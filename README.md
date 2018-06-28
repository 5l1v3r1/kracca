# About
kracca generates a list of possible passwords for a person or company, given 
relevant information like name, address, phone, etc. 

## Example 
```
Name: John Doe
DOB: 13 Feb 1999
Generated passwords: 
johndoe 
j0hnd03
j0hn123 
johndoe199
1321999
john1999
Doe1999
JohnDoe1321999
etc...
```

# Usage 
In order for kracca to generate the most relevant password sets, it must be given accurate data. The following fields are recommended: 
* Name of target company or target person 
* Date of birth for person 
* Address for company
* Phone number of enterprise or person
* The current year for enterprise 

The more information you feed kracca, the higher the chance that kracca will generate a correct password. **kracca is only as good as the information you give it.**
This program might eat up your RAM, so please don't run this on a microwave

### keynums.txt 

keynums is a pre-made list of numbers that are likely to be part of a password. You can add numbers that are relevant to the target, such as DOB, numbers of special personal or organizational significance, etc, to this list. 

### keywords.txt 

keywords is a pre-made wordlist that is a compilation of cracklib's wordlist, /usr/share/dict words for American and British English and Spanish. As with keynums, you can add words relevant to the target in order to increase accuracy.

oh, and FUCK SIX
