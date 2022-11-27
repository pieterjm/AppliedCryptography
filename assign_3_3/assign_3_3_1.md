Generating a private key:

```
openssl genrsa -help
```

```
openssl genrsa 2048 > randomkey.prv
```

Creating a public key from a private key

```
openssl rsa -in randomkey.prv -pubout -outform PEM -out random.pub
```

PEM (originally “Privacy Enhanced Mail”) is the most common format for X.509 certificates. X.509 is the standard for public key certificates.

