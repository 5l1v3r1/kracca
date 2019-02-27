import itertools 
import threading 
import time 
import sys 
import re

def animate(): 
    for c in itertools.cycle(['|', '/', '-', '\\']): 
        if done:
            break 
        sys.stdout.write('\rgenerating permutations....' + c)
        sys.stdout.flush() 
        time.sleep(0.1)
    sys.stdout.flush()
    sys.stdout.write('\rDone!\n')

def docurrentyear(currentyear, mode, result, keywords, keynums, pooltxt): 
    pool = []
    pools = open(pooltxt, "+a")
    x = [int(i) for i in str(currentyear)]
    for j in itertools.combinations(x, len(x)): 
        pool.append(j) 
    for i in pool: 
        pools.append(str(i) + "\n")

def doaddress(address, mode, result, keywords, keynums, pooltxt): 
    pool = [] 
    names = ['drive', 'circle', 'road', 'highway', 'way', 'terrace', 'pike', 'street', 'trail', 'lane', 'line', 'avenue', 'alley', 'byway', 'cross', 'passage', 'turnpike', 'parkway', 'court', 'boulevard', 'place', 'track', 'passage', 'route']
    # Format should be: address[0] = street number
    #                   address[1] = street name 
    pools = open(pooltxt, "+a")
    address = address.split(" ")
    for i in names: 
        if i.title() in address: 
            address.remove(i.title()) 
    streetnumber = int(address[0]) 
    streetname = str(address[1]) 
    pool.append(streetnumber) 
    pool.append(streetname.upper()) 
    pool.append(streetname.lower()) 
    pool.append(streetname.upper()) 
    
    for i in pool: 
        pools.write(str(i) + "\n")

def dodob(dob, mode, result, keywords, keynums, pooltxt): 
    pool = [] 
    pools = open(pooltxt, "+a") 
    dob = dob.split("/") 
    months = { 1 : "January", 2 : "Feburary", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
    # dd/mm/yyyy
    day = dob[0].lstrip('0')
    month = dob[1].lstrip('0') 
    year = dob[2]
    shortmonth = months[month]
    shortmonth = shortmonth[:3]
    pool.append(''.join(year))
    pool.append(''.join(month))
    pool.append(''.join(day))
    pool.append(shortmonth) 

    for i in pool: 
        pools.write(i + "\n")

def doemails(emails, mode, result, keywords, keynums, pooltxt): 
    # parses email to extract data
    # example: mikevirus@aol.com 
    # names = ['mike', 'virus', 'mikevirus'] 
    # names are added to pool
    pool = [] 
    emails = emails.split(" ")
    for i in emails:
        i = i.split("@")
        i = i[:1]
    # example: mikevirus@aol.com 
    # after split(): mikevirus 
    # mike is a word! pool = ['mike', 'MIKE', 'Mike'] 
    # virus is a word! pool = ['mike', 'MIKE', 'Mike', 'virus', 'VIRUS', 'Virus']
    for email in emails:
        pool.append(''.join(email).upper().rstrip()) 
        pool.append(''.join(email).title().rstrip())
        if any(char.isdigit() for char in email): 
            number = re.sub('[^0-9]','',email)
            pool.append(str(number)) 
   # makes strings like mikevirus, MIKEVIRUS, etc possible. thx python! 
    for permutation in itertools.permutations(pool, 2): 
         pool.append(''.join(permutation)) 
    pools = open(pooltxt, "+a")
    for i in pool:
        pools.write(str(i) + "\n")

def dofamily(family, mode, result, keywords, keynums, pooltxt): 
    pool = [] 
    pools = open(pooltxt, "+a")
    names = family.split(" ") 
    for name in names: 
        pool.append(name.upper())
        pool.append(name.lower())
    for i in pool: 
        pools.write(i + "\n")

def dophone(phone, mode, result, keywords, keynums, pooltxt): 
    pool = []
    magicnums = open(keynums, "r")
    pools = open(pooltxt, "+a")
    pool.append(str(phone))
    for i in pool:
        pools.write(str(i) + "\n")

def doname(name, mode, result, keywords, keynums, pooltxt): 
    # generates initial permutations of a name,  
    pool = []
    if " " in name:
        fullname = name.split(" ") # split name into elements in an array
    else: 
        fullname = [] 
        fullname.append(name)
    pool.append(name.title()) 
    pool.append(name.swapcase()) 
    pool.append(name.upper()) 
    pool.append(name.lower()) 
    pool.append(''.join(fullname).upper())
    pool.append(''.join(fullname).lower())
    for i in range(len(fullname)): 
        pool.append(fullname[i])
    initials = []
    for i in fullname: 
        initials.append(i[0])
    pool.append(''.join(initials).upper())
    pool.append(''.join(initials).lower())
    pool.append(''.join(initials[1:]) + name)
    pools = open(pooltxt, "+a")

    if mode == "--enterprise":
        partialLower = [i.lower() for i in fullname[1:]] 
        partialUpper = [i.upper() for i in fullname[1:]]
        partialUpper.append(fullname[0]) 
        pool.append(''.join(partialUpper)) 
        pool.append(''.join(partialLower))
        pool.append(''.join(partialUpper).upper()) # THUGCROWDAL
        pool.append(''.join(partialLower).lower()) # thugcrowdal 
    for i in fullname: 
        pool.append(i.title()) 
        pool.append(i.swapcase()) 
        pool.append(i.upper()) 
        pool.append(i.lower())
    for i in pool: 
        pools.write(i + "\n")

def doaliases(aliases, mode, result, keywords, keynums, pooltxt):
    pool = [] 
    pools = open(pooltxt, "+a")
    dictionary = open(keywords, "r")
    aliases = aliases.split(" ")
    for i in aliases: 
        pool.append(i.upper()) 
        pool.append(i.lower()) 
        pool.append(i.title())
        pool.append(xify(i))
        tmp = leetify(i) 
        for x in tmp: 
            pool.append(x.upper())
            pool.append(x.lower())
            pool.append(x.title())
        if "_" in aliases: 
            i = i.split(" ")
    for i in pool:
        pools.write(i + "\n")

def xify(word): 
    vowels = ["a", "e", "i", "o", "u"]
    x = ""
    for i in word: 
        if i.lower() in vowels: 
            x += "x"
        else:
            x += i
    return x

def leetify(word): 
    LEETERS = {
            "i" : "1!|",
            "I" : "1!|",
            "o" : "0",
            "O" : "0", 
            "s" : "5$",
            "S" : "5$",
            "e" : "3",
            "E" : "3",
            "a" : "4@",
            "A" : "4@",
            "t" : "7",
            "T" : "7", 
            "c" : "([<",
            "C" : "([<"
            } 
    possibilities = [z + LEETERS.get(z, "") for z in word] 
    tmp = []
    for sub in itertools.product(*possibilities): 
        tmp.append("".join(sub))
    return tmp

def permutations(result, keywords, keynums, pooltxt, capital, numbers):  
    global done
    done = False
    # given a pool of possibilities, combine with data to add to results
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    pooltxt = open(pooltxt, "r") 
    pool = [] 
    for i in pooltxt: 
        pool.append(i)
    temppool = pool[:] # copies pool 
    t = threading.Thread(target=animate) 
    t.start()
    x = []
    for i in range(len(pool)): 
        for j in itertools.combinations(pool, 2):
            temppool.append(''.join(j).rstrip())
        for y in itertools.combinations(pool, 3):
            temppool.append(''.join(y).rstrip())
    for i in x: 
        temppool.append(''.join(i))
    for word in pool: 
        if " " in word: 
            for letter in alphabet: 
                temppool.append(word.replace(" ", letter))
            temppool.extend([word.replace(" ", str(x)) for x in range(1, 1000)])
        else: 
            temppool.extend([word + str(x) for x in range(1,1000)])
            temppool.extend([str(x) + word for x in range(1, 1000)])
            with open(keynums, "r") as magicnums: 
                for magicnum in magicnums: 
                    temppool.append(word + str(magicnum).rstrip()) 
                    temppool.append(str(magicnum) + word) 
                magicnums.close() 
            with open(keywords, "r") as magicwords:
                for magicword in magicwords: 
                    temppool.append(word.rstrip() + magicword.rstrip().upper())
                    temppool.append(word.rstrip() + magicword.rstrip().lower())
                    temppool.append(magicword.rstrip() + word)
                magicwords.close()
            for letter in alphabet: 
                temppool.append(word.rstrip() + letter)
                temppool.append(letter + word.rstrip())
    for word in temppool: 
        tmp = leetify(str(word).rstrip())
        for word in tmp: 
            temppool.append(word)
    for z in x: 
        temppool.append(z)
    for permutation in temppool: 
        if capital == True and numbers == False: 
            if permutation.isalnum() == True: 
                pass
            else: 
                temppool.remove(permutation) 
        elif capital == True: 
            if bool(re.match('^[A-Z]+$', permutation)) == True: 
                pass
            else: 
                temppool.remove(permutation) 
        elif numbers == True: 
            if bool(re.match('^[0-9]+$', permutation)) == True: 
                pass
            else: 
                temppool.remove(permutation) 
        else: 
            pass
    pool = list(dict.fromkeys(temppool)) # save changes to pool 
    results = open(result, "+w")
    for i in pool:
        results.write(str(i).rstrip() + "\n")
    time.sleep(5)
    done = True
    magicnums.close()
    magicwords.close()
    results.close() 
