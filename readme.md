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



### Les 4

Podcast met interview van Whitfdield Diffy (https://www.youtube.com/watch?v=uEnvp714H5U)
https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Practical_attacks_on_Internet_traffic
DH 2048 key size en Ephemeral
https://www.youtube.com/watch?v=NmM9HA2MQGI
https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2021/januari/19/ict-beveiligingsrichtlijnen-voor-transport-layer-security-2.1/ICT-beveiligingsrichtlijnen+voor+Transport+Layer+Security+v2.1.pdf

Ephemeral Diffie-Hellman (DHE in the context of TLS) differs from the static Diffie-Hellman (DH) in the way that static Diffie-Hellman key exchanges always use the same Diffie-Hellman private keys. So, each time the same parties do a DH key exchange, they end up with the same shared secret.

When a key exchange uses Ephemeral Diffie-Hellman a temporary DH key is generated for every connection and thus the same key is never used twice. This enables Forward Secrecy (FS), which means that if the long-term private key of the server gets leaked, past communication is still secure.

This distinction also holds for the Elliptic Curve variants ECDHE (ephemeral, provides Forward Secrecy) and ECDH (static).

Due to increasing concern about pervasive surveillance, key exchanges that provide Forward Secrecy are recommended, see for example RFC 7525, section 6.3.


