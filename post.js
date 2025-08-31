fetch("url",{
    method:'POST',
    headers:{
        'Content-Type':'application/xml'
    },
    body:`<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
	<productId>1</productId>
	<storeId>3</storeId>
</stockCheck>`
})
.then(res=>res.text())
.then(console.log)
.then(console.error);