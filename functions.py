def doname(name, mode, result, keywords, keynums): 
    pool = []
    fullname = name.split(" ") #split name into elements in an array
    pool.append(name.title()) 
    pool.append(name..swapcase()) 
    pool.append(name..upper()) 
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

def permutations(pool, keywords, keynums, results):  
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    leetvowel = {"o" : "0", "a" : "4", "e" : "3", "i" : "1", "O" : "0", "A" : "4", "E" : "3", "I" : "1"}
    magicwords = open(keywords, "r") 
    magicnums = open(keynums, "r") 
    
