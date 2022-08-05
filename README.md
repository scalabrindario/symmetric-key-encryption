# Symmetric Key Encryption

## Introduction
In the last decades, digital communications intensified thanks to the introduction of the smartphone technology, which allowed the majority of the population to gain access to the internet anywhere, anytime. With it, chat messaging apps, such as WhatsApp, WeChat and Telegram gained traction, to the point of dominating the communication landscape worldwide. Due to the rapid expansion of these digital technologies, cyber security has become a widespread issue. The recent scandal of Cambridge Analytica and the leaks of Edward Snowden shed light on the need to improve IT communications’ safety standards.

On these topics there are many issues, but we will focus mainly on a security mechanism: encryption.

## Encryption
Wikipedia defines encryption as “*the process of encoding information*”. This process transforms the original message, also known as plain text, into an alternative form, known as cipher text. This conversion should provide secrecy to the sender and the receiver and so prevent third parties to be able to read information. There are two types of encryption: public key algorithm and symmetric key algorithm. We will focus only on the latter.

Symmetric key is an algorithm that use a key to encrypt and decrypt a message. A key is a secret shared between the sender and the receiver. This kind of algorithm is based on transposition and substitution techniques.
Nowadays, modern algorithms try to achieve two features:
- Fixed size keys, which implies that the key does not need to be as long as the plain text.
- Little statistical correlation between plain text and cipher text, which is needed in order to render computationally impossible to recover the plain text, given the cipher text.

AES is the encryption algorithm which provides almost zero statistical correlation, although the only 100% safe encryption algorithm is One-Time-Pad. One-Time-Pad, however, cannot be used due to the problem of exchanging a key, which is longer than the plain text and must be transmitted using a secure channel.
Statistical correlation is the problem that affects the cipher text which we were given. We will exploit this issue in order to achieve our goal of recovering the plain text. It is useful to point out that in our project we will do a simplified attack because the cipher text is very long and only letters have been encrypted.

## The project in pills
The aim of this project is to decrypt a cipher text, a text that has been encrypted using a substitution method. In order to verify whether we were successful in the procedure, we will compare the digest we were given at the start of the project by the professor, with the digest we produced using a SHA256 hashing function on the cipher text we just decrypted. If the two digests coincide, it will mean that the procedure was correct. It could happen that the two digests will never coincide, and so the user should manually swap the wrong letters.

## Procedure
1. Frequency Analysis
2. Creation of candidate plain text
3. Verification of the digest of the candidate plain text
4. Counting and computing percentage of bigrams in corpus text
5. Computing score bigrams in candidate plain text
6. Swapping the best letter in the candidate text according to bigram analysis
7. Computing hash of the new candidate plain text

This procedure is iterative, repeating the process until it substitutes all the letters of the alphabet. In case the digest of the plain text will never correspond to the digest given by the professor, the program will return the candidate plain text decrypted at the best of its capabilities

<p align="center"><img src="https://drive.google.com/uc?id=1bhimTPcGoS9om42PrbdUbcgz0qDwWGm_" width="600"/></p>



## Main Difficulties
The main difficulty that we encountered was using the bigram score to find out the correct plain text. In an early version of the project, we only used the frequency analysis and then printed out the candidate plain text. This implied a long manual swapping process.
This made for a clunky process with little to no automatization and very unprofessional code, requiring constant supervision from the user in order to understand what was the key for each letter.

We rendered the process smoother thanks to the implementation of the bigram frequency analysis and the subsequent bigram score.

We must remark that to get to the final process, it was not easy to elaborate the final code, because we encountered many hurdles. Initially, the process took way too much time, because we were using the whole cipher text, which slowed down the process by a lot.

Furthermore, we were counting the bigrams after each iteration at first, computing the frequency, and this process was executed for each letter swap, namely 2626 times, requiring several hours to complete. Through code optimizations we managed to polish the process up to its current state, requiring less than half a minute to decrypt the cipher text as best as it can.

## Conclusion
Despite the simplicity of the encryption (only the letters were encrypted, leaving spaces and punctuation untouched), finding the right solution was not easy. During this project we had a chance to get a hand-on feel for the topics touched during the lessons. It made us realize that encryption and hashing are vital nowadays for security services and mechanisms.





