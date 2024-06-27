Vigenere
Program to decrypt/encrypt a passage using Vigenere cipher technique.

Just run the file and it will prompt you to make a choice betweeen encrypting or decrypting

In both the encrypting or decrypting choice you will see the following input questions:

The first keyword, which creates the alphabet "top" line of the matrix. The keyword here currently must contain only one instance of each letter of the alphabet. For example you can use "Help" but not "Helper" since "Helper" has two e's.

The second keyword, which creates the lines undeaneath the top line. This finishes the "matrix" used for encoding/decoding. You can use any word here, it can contain more than one instance of a letter. So you could use "Helper" here.

The passage to encrypt/decrypt.

You can take a look at this rather quick YouTube video to see the basics of how Vigenere ciphers work.

https://www.youtube.com/watch?v=0Pm2PrxmU38

I would suggest you try first doing something where you know the keys, as well as the encrypted/decrypted passages just to test that it is working. Something like the first Kryptos passage (K1) from the CIA Kryptos sculpture which is listed below. Please note that "illusion" in the text below is intentionally misspelled:

ENCRYPT
First Key: KRYPTOS
Second Key: PALIMPSEST
Enter passage you wish to encrypt: Between subtle shading and the absence of light lies the nuance of iqlusion

Encrypted passage you should get returned: EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD

DECRYPT
First Key: KRYPTOS
Second Key: PALIMPSEST
Enter passage you wish to decrypt: EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD

Decrypted passage you should get returned:
Betweensubtleshadingandtheabsenceoflightliesthenuanceofiqlusion
