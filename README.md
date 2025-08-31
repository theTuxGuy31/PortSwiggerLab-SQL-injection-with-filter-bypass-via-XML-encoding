# SQL Injection with XML Encoding Filter Bypass

This repository contains tools and payloads for demonstrating SQL injection attacks that bypass filters using XML encoding techniques. The materials are designed for educational purposes and security research.

## Target Lab

This repository is designed to work with the PortSwigger Web Security Academy lab:

**Lab:** SQL injection with filter bypass via XML encoding  
**Link:** https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding

## Video Tutorial

Youtube link: https://youtu.be/BgrF-mWw9Zk?si=izERzq2pAcw3J6rd

## Repository Contents

### Core Files

- **`hex_encoder.py`** - HTML hex entity encoder/decoder utility
- **`payloads.txt`** - SQL injection payloads for testing
- **`post.js`** - JavaScript code for making XML POST requests
- **`readme.md`** - Basic repository information

## Tools

### HTML Hex Entity Encoder (`hex_encoder.py`)

A Python utility that converts text to HTML hex entities (`&#xHH;` format) and vice versa. This tool is useful for encoding payloads to bypass input filters.

#### Features
- Encode text to HTML hex entities
- Decode HTML hex entities back to text
- Interactive demo mode
- Command-line interface
- File input/output support

#### Usage

**Interactive Mode:**
```bash
python3 hex_encoder.py
```

**Command Line:**
```bash
# Encode text
python3 hex_encoder.py encode -i "Hello World"

# Decode entities
python3 hex_encoder.py decode -i "&#x48;&#x65;&#x6C;&#x6C;&#x6F;"

# Show character mapping
python3 hex_encoder.py demo -i "SQL"

# Process files
python3 hex_encoder.py encode -f input.txt -o output.txt
```

### SQL Injection Payloads (`payloads.txt`)

Contains common SQL injection payloads for:
- Discovering table column counts using UNION SELECT
- Extracting data from user tables
- Concatenating username and password fields

### XML POST Request (`post.js`)

JavaScript code demonstrating how to send XML POST requests that can be used to test XML-based endpoints for injection vulnerabilities.

## Educational Purpose

This repository is intended for:
- Security research and education
- Penetration testing practice
- Understanding XML encoding bypass techniques
- Learning about SQL injection mitigation

## Legal Disclaimer

**IMPORTANT:** These tools and techniques should only be used on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal and unethical.

- Use only on authorized targets
- Respect responsible disclosure practices
- Follow applicable laws and regulations
- Use for educational and defensive purposes only

## Mitigation

To protect against these types of attacks:

1. **Use parameterized queries/prepared statements**
2. **Implement proper input validation**
3. **Apply output encoding**
4. **Use least privilege database access**
5. **Implement Web Application Firewalls (WAF)**
6. **Regular security testing and code review**

## Additional Resources

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)


## License

This project is for educational purposes. Please use responsibly and in accordance with applicable laws.
