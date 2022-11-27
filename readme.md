# Applied Cryptography

## Handy python functions


| Function  | Purpose  | Example  |
|---|---|---|
| ord  | Convert character to ASCII number  | `ord('a')` returns 97  |
| chr  | Convert integer to corresponding ASCII character   | `chr(97)` returns 'a'  |
| hex  | Convert a number to hexadecimal string, prefixed with '0x'  | `hex(255)` returns '0xff'   |
| int(..., base=16)  | Convert a hex string to decimal | `int('0xff',base=16)` returns 255 |  
| bytes | Returns an immutable bytes object |  `bytes('Hello, world!','utf-8')` returns a byte string:  b'Hello, world!' |
| str.decode('utf-8') | converts byte string to string | `b'This is a test'.decode('utf-8')` returns: 'This is a test' |


