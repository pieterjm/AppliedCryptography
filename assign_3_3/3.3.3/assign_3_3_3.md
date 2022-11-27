To verify a signature with openssl, use the following command

```
openssl dgst -verify user.pub  -signature file1.sign -binary file.txt
```

Deze geeft als resultaat Verify OK

het andere signature geeft een signature fout

```
openssl dgst -verify user.pub  -signature file2.sign -binary file.txt
```