"""
HTML Hex Entity Encoder
Converts text to HTML hex entities (&#xHH; format).
"""

import argparse
import sys
import re

class HTMLHexEncoder:
    """A class for encoding and decoding HTML hex entities."""
    
    @staticmethod
    def encode_to_html_hex_entities(content: str) -> str:
        """
        Encode each character to HTML hex entity format (&#xHH;).
        
        Args:
            content (str): Content to encode
            
        Returns:
            str: HTML hex entities representation
        """
        result = []
        for char in content:
            # Get Unicode code point and convert to hex
            code_point = ord(char)
            hex_value = format(code_point, 'X')  # Uppercase hex
            result.append(f"&#x{hex_value};")
        return ''.join(result)
    
    @staticmethod
    def decode_from_html_hex_entities(content: str) -> str:
        """
        Decode HTML hex entities back to regular characters.
        
        Args:
            content (str): Content with HTML hex entities
            
        Returns:
            str: Decoded content
        """
        def replace_entity(match):
            hex_value = match.group(1)
            try:
                code_point = int(hex_value, 16)
                return chr(code_point)
            except (ValueError, OverflowError):
                return match.group(0)  # Return original if invalid
        
        # Pattern to match &#xHH; or &#xHHHH; etc.
        pattern = r'&#x([0-9A-Fa-f]+);'
        return re.sub(pattern, replace_entity, content)
    
    @staticmethod
    def char_to_hex_entity_demo(content: str) -> str:
        """
        Show character-by-character hex entity conversion.
        
        Args:
            content (str): Content to demonstrate
            
        Returns:
            str: Formatted demonstration
        """
        result = []
        for char in content:
            code_point = ord(char)
            hex_value = format(code_point, 'X')
            if char.isprintable() and char != ' ':
                result.append(f"{char} = &#x{hex_value};")
            elif char == ' ':
                result.append(f"[SPACE] = &#x{hex_value};")
            elif char == '\n':
                result.append(f"[NEWLINE] = &#x{hex_value};")
            elif char == '\t':
                result.append(f"[TAB] = &#x{hex_value};")
            else:
                result.append(f"[{repr(char)}] = &#x{hex_value};")
        return '\n'.join(result)

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description='HTML Hex Entity Encoder/Decoder')
    parser.add_argument('action', choices=['encode', 'decode', 'demo'], 
                       help='Action: encode (to hex entities), decode (from hex entities), demo (show mapping)')
    parser.add_argument('-i', '--input', type=str, 
                       help='Input string (if not provided, reads from stdin)')
    parser.add_argument('-f', '--file', type=str,
                       help='Input file path')
    parser.add_argument('-o', '--output', type=str,
                       help='Output file path (if not provided, prints to stdout)')
    parser.add_argument('-e', '--encoding', type=str, default='utf-8',
                       help='File encoding (default: utf-8)')
    
    args = parser.parse_args()
    
    encoder = HTMLHexEncoder()
    
    # Get input content
    if args.file:
        try:
            with open(args.file, 'r', encoding=args.encoding) as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.", file=sys.stderr)
            sys.exit(1)
        except UnicodeDecodeError as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.input:
        content = args.input
    else:
        # Read from stdin
        content = sys.stdin.read()
    
    # Process content
    try:
        if args.action == 'encode':
            result = encoder.encode_to_html_hex_entities(content)
        elif args.action == 'decode':
            result = encoder.decode_from_html_hex_entities(content)
        elif args.action == 'demo':
            result = encoder.char_to_hex_entity_demo(content)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Output result
    if args.output:
        try:
            with open(args.output, 'w', encoding=args.encoding) as f:
                f.write(result)
            print(f"Output written to '{args.output}'")
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(result)

# Interactive mode and demonstrations
if __name__ == "__main__":
    # If running as script with arguments, use command-line interface
    if len(sys.argv) > 1:
        main()
    else:
        # Interactive demo mode
        encoder = HTMLHexEncoder()
        
        print("HTML Hex Entity Encoder")
        print("=" * 30)
        print("Convert characters to &#xHH; format")
        print("Type 'quit' to exit\n")
        
        while True:
            try:
                user_input = input("Enter text: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                elif not user_input:
                    continue
                
                # Show both formats
                entities = encoder.encode_to_html_hex_entities(user_input)
                print(f"HTML Entities: {entities}")
                
                demo = encoder.char_to_hex_entity_demo(user_input)
                print("Character Mapping:")
                print(demo)
                print()
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
        
        print("\nCommand-line usage examples:")
        print("  python script.py encode -i 'Hello'")
        print("  python script.py demo -i 'S'")
        print("  python script.py decode -i '&#x48;&#x65;&#x6C;&#x6C;&#x6F;'")
