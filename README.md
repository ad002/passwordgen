# passwordgen
A repo for my own passwordgenerator. First in Python, then on my Website (passwordgen.co.nf)

RESEARCH
https://en.wikipedia.org/wiki/Password_strength

Based on Wikipedia password strength is a "measure of the effectiveness of a password against
guessing or a brute-fore attack. In its usual form, it estimates how many trials an attacker 
who doesn't have direct access to the password would need, on averagem to guess it correcty"

**Entropy as a measure of password strength**
Instead of the number of guesses needed to find the password with certainity, the base-2 logarithm
pf that number is given, which is the number of "entropy bits" in a password.

A password with an entropy of 42 bits calculated in this way would be as strong as a string
of 42 bits chosen randomly, for example by a fair coin toss. 

Put another way, a password with an entropy of 42 bits would require 2^42 (4.398.046.511.104)
attempts to exhaust all possibilities during a brute force search. 

Thus, by increasing the entropy of the password by one bit, the number of guesses required
doubles, making a crack twice as difficoult. 


https://www.betterbuys.com/estimating-password-cracking-times/

Amount of time needed to crack passwords:
7 characters 	.29 miliseconds
8 characters	5 hours
9 characters	5 days
10 characters	4 months 
11 characters	1 decade
12 characters	2 centuries

Based on https://strongpasswordgenerator.com/ a strong password will have at least 
- 15 characters
- uppercase letters
- lowercase letters
- numbers
- symbols 


PROGRAM
1. Let user choose whether he wants a chain, vault or fortress like password
2. based on his input, a chain password will be 16 characters, a vault will have 32 characters  
   and the fortress will have 64 characters
3. Choose random characters and symbols from charset
4. Alterate basic program with option to choose whether he wants upper-, lowercase etc., 
   this will then be passwordgen2.py
