import itertools 
import threading 
import time 
import sys 

# lolcow is the koolest kid on the block, did you know his mom lets him bring as many Lunchables as he wants to school? `

def animate(): 
    for c in itertools.cycle(['|', '/', '-', '\\']): 
        if done:
            break 
        sys.stdout.write('\rgenerating permutations....' + c)
        sys.stdout.flush() 
        time.sleep(0.1)
    sys.stdout.write('\rDone!       ')

def doname(name, mode, result, keywords, keynums): 
    pool = []
    fullname = name.split(" ") # split name into elements in an array
    pool.append(name.title()) 
    pool.append(name.swapcase()) 
    pool.append(name.upper()) 
    pool.append(name.lower()) 
    
    initials = []
    for i in fullname: 
        initials.append(i[0])
    pool.append(str(initials).upper())
    pool.append(str(initials).lower())

    for i in fullname: 
        pool.append(i.title()) 
        pool.append(i.swapcase()) 
        pool.append(i.upper()) 
        pool.append(i.lower())
    permutations(pool)

def leetify(word): 
    leetletters = {"o" : "0", "a" : "4", "e" : "3", "i" : "1", "s" : "5", "t", "7" "O" : "0", "A" : "4", "E" : "3", "I" : "1", "s" : "5", "T", "7"}
    for i in word:
         if i in leetletters: 
             i = leetletters[i] 

def permutations(pool, keywords, keynums, results):  
    done = False
    # given a pool of possibilities, combine with data to add to results
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    magicwords = open(keywords, "r") 
    magicnums = open(keynums, "r") 
    temppool = pool[:] # copies pool 
    t = threading.Thread(target=animate) 
    t.start()

    for word in temppool: 
        if " " in word: 
            for num in range(1, 1000): 
                temppool.append(word.replace(" ", num)
            magicnums.seek(0)
            for magicnum in magicnums:
               temppool.append(word.replace(" ", magicnum)
            magicwords.seek(0)
            for magicword in magicwords: 
                temppool.append(word.replace(" ", magicword) 
        else: 
            for num in range(1, 1000): 
                temppool.append(word + num) 
                temppool.append(num + word) 
            magicnums.seek(0) 
            for magicnum in magicnums: 
                temppool.append(word + magicnum) 
                temppool.append(magicnum + word) 
            magicwords.seek(0)
            for magicword in magicwords: 
                temppool.append(word + magicword) 
                temppool.append(magicword + word)

        temppool.append(leetify(word))
    pool = temppool[:] # save changes to pool 
    result = open(results, "w")
    for i in pool:
       result.write(i)
    time.sleep(5)
    done = True

