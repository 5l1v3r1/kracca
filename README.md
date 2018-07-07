# About
kracca generates a list of possible passwords for a person or company, given 
relevant information like name, address, phone, etc. 

## Example 
```
Name: John Doe
DOB: 13 Feb 1999
Email: seahawks1999@aol.com
Generated passwords: 
johndoe 
J0hnd03
seahawks1999
john1999
jd1999
132199
s34h4wks
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

### Requirements 
* At least 4GB RAM 
* At least an i3 processor 
* 1-2 GB of free storage

### Upcoming
* A better wordlist (current one is every single word in the English language, hope to replace this with top 2000 words used in passwords for less overhead) 
* Intelligent identification and classification of interesting strings / numbers used consistently across emails, aliases, etc
* Organized wordlists by topic, eg infosec, sport, video games, etc. 
* Multithreading (this will never happen i am too lazy)
