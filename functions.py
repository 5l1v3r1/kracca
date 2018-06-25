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

# lolcow is the koolest kid on the block, did you know his mom lets him bring as many Lunchables as he wants to school? `

'''
 ______   __  __     ______     __         __     ______             
/\  == \ /\ \/\ \   /\  == \   /\ \       /\ \   /\  ___\            
\ \  _-/ \ \ \_\ \  \ \  __<   \ \ \____  \ \ \  \ \ \____           
 \ \_\    \ \_____\  \ \_____\  \ \_____\  \ \_\  \ \_____\          
  \/_/     \/_____/   \/_____/   \/_____/   \/_/   \/_____/          
                                                                     
 ______     __   __     ______     __    __     __  __               
/\  ___\   /\ "-.\ \   /\  ___\   /\ "-./  \   /\ \_\ \              
\ \  __\   \ \ \-.  \  \ \  __\   \ \ \-./\ \  \ \____ \             
 \ \_____\  \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \/\_____\            
  \/_____/   \/_/ \/_/   \/_____/   \/_/  \/_/   \/_____/            
                                                                     
 __   __     __  __     __    __     ______     ______     ______    
/\ "-.\ \   /\ \/\ \   /\ "-./  \   /\  == \   /\  ___\   /\  == \   
\ \ \-.  \  \ \ \_\ \  \ \ \-./\ \  \ \  __<   \ \  __\   \ \  __<   
 \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/ \/_/   \/_____/   \/_/  \/_/   \/_____/   \/_____/   \/_/ /_/ 
                                                                     
 ______     ______     ______     ______                             
/\___  \   /\  ___\   /\  == \   /\  __ \                            
\/_/  /__  \ \  __\   \ \  __<   \ \ \/\ \                           
  /\_____\  \ \_____\  \ \_\ \_\  \ \_____\                          
  \/_____/   \/_____/   \/_/ /_/   \/_____/

	the real irc whitehat warlordz
'''

def doemail(email, mode, result, keywords, keynums, pooltxt): 
    # parses email to extract data
    # example: mikevirus@aol.com 
    # names = ['mike', 'virus', 'mikevirus'] 
    # names are added to pool
    pool = [] 
    email = email.split("@")
    email = email[1:] # remove everything after @ 
    magicwords = open(keywords, "r") 
    magicnums = open(keynums, "r")
    # example: mikevirus@aol.com 
    # after split(): mikevirus 
    # mike is a word! pool = ['mike', 'MIKE', 'Mike'] 
    # virus is a word! pool = ['mike', 'MIKE', 'Mike', 'virus', 'VIRUS', 'Virus']

    for magicword in magicwords: 
        upper = magicword.upper() 
        lower = magicword.lower() 
        cap = magicword.title() 
        if upper in email or lower in email or cap in email: 
            pool.append(upper) 
            pool.append(lower) 
            pool.append(cap)
    if any(char.isdigit() for char in email): 
        number = re.sub('[^0-9]','',email)
        pool.append(number) 
    magicnums.close() 
    magicwords.close() 
   # makes strings like mikevirus, MIKEVIRUS, etc possible. thx python! 
    for permutation in itertools.permutations(pool, 2): 
         pool.append(permutation) 
    pools = open(pooltxt, "+a")
    for i in pool:
        pools.write(i + "\n")

def dophone(phone, mode, result, keywords, keynums, pooltxt): 
    # generates all statistically plausible permutations of a phone number: 
    # example: 1234567890
    # permutations: 123456789, 123, 1234, 7890, etc.
    # the reason why i'm not feeding this into itertools and generating another
    # 50,000 possibilities is because people never put their phone number in 
    # random order when using it in a password; they tend to put it in full, 
    # use the first x digits, but rarely in reverse.
    
    pool = []
    magicnums = open(keynums, "r")
    pools = open(pooltxt, "+a")
    skip = 0
    for i in range(len(phone)): 
        pool.append(''.join(str(phone[skip:])))
        skip = skip + 1
    for num in pool: 
        pools.write(str(num))

def doname(name, mode, result, keywords, keynums, pooltxt): 
    # generates initial permutations of a name, 
   
    pool = []
    fullname = name.split(" ") # split name into elements in an array
    pool.append(name.title()) 
    pool.append(name.swapcase()) 
    pool.append(name.upper()) 
    pool.append(name.lower()) 
    pool.append(''.join(fullname).upper())
    pool.append(''.join(fullname).lower())
    initials = []
    for i in fullname: 
        initials.append(i[0])
    pool.append(''.join(initials).upper())
    pool.append(''.join(initials).lower())
    pools = open(pooltxt, "+a")
    # The following code is a little opaque, so i'll try to explain it 
    # Imagine we are targeting a company named Thugcrowd Analytics Limited
    # Naming conventions mean that possible permutations could not only be TAL, but could also be ThugcrowdAL, etc, etc 
    # The following block handles this exception 

    if mode == "--enterprise":
        partialUpper = [] 
        partialLower = []
        partialUpper.append(fullname[0]) 
        partialLower = [] 
        for i in fullname[1:]: 
            partialUpper.append(i.upper()) # partialUpper = ['Thugcrowd', 'A', 'L'] 
        for i in fullname[1:]:
            partialLower.append(i.lower()) # partialLower = ['Thugcrowd', 'a', 'l'] 
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

def leetify(word): 
    leetletters = {"o" : "0", "a" : "4", "e" : "3", "i" : "1", "s" : "5", "t" : "7", "O" : "0", "A" : "4", "E" : "3", "I" : "1", "s" : "5", "T" : "7"}
    for i in word:
         if i in leetletters: 
             i = leetletters[i] 
    return word

def permutations(result, keywords, keynums, pooltxt):  
    global done
    done = False
    # given a pool of possibilities, combine with data to add to results
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    magicwords = open(keywords, "r") 
    magicnums = open(keynums, "r") 
    pooltxt = open(pooltxt, "r") 
    pool = [] 
    for i in pooltxt: 
        pool.append(i)
    temppool = pool[:] # copies pool 
    t = threading.Thread(target=animate) 
    t.start()

    for word in pool: 
        if " " in word: 
            for num in range(1, 1000): 
                temppool.append(word.replace(" ", str(num).rstrip()))
            magicnums.seek(0)
            for magicnum in magicnums:
               temppool.append(word.replace(" ", str(magicnum).rstrip()))
            magicwords.seek(0)
            for magicword in magicwords: 
                temppool.append(word.replace(" ", magicword.rstrip())) 
            for letter in alphabet: 
                temppool.append(word.replace(" ", letter))
        else: 
            for num in range(1, 1000): 
                temppool.append(word + str(num)) 
                temppool.append(str(num) + word) 
            magicnums.seek(0) 
            for magicnum in magicnums: 
                temppool.append(word + str(magicnum).rstrip()) 
                temppool.append(str(magicnum) + word) 
            magicwords.seek(0)
            for magicword in magicwords: 
                temppool.append(word.rstrip() + magicword.rstrip()) 
                temppool.append(magicword.rstrip() + word)
            for letter in alphabet: 
                temppool.append(word.rstrip() + letter)
                temppool.append(letter + word.strip())
        temppool.append(leetify(word))
    pool = temppool[:] # save changes to pool 
    results = open(result, "+w")
    for i in pool:
        print(i)
        results.write(str(i).rstrip() + "\n")
    time.sleep(5)
    done = True
    magicnums.close()
    magicwords.close()
    results.close() 
