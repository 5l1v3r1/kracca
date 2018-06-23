from functions import * 

class Info: 
    def __init__(self, **kwargs): 
        self.name = kwargs["name"] if "name" in kwargs else None 
        self.currentyear = kwargs["currentyear"] if "currentyear" in kwargs else None 
        self.address = kwargs["address"] if "address" in kwargs else None 
        self.motto = kwargs["motto"] if "motto" in kwargs else None 
        self.phone = kwargs["phone"] if "phone" in kwargs else None 
        self.dob = kwargs["dob"] if "dob" in kwargs else None
        self.email = kwargs["email"] if "email" in kwargs else None 
        self.family = kwargs["family"] if "family" in kwargs else None 
        self.mode = kwargs["--enterprise"] if mode in kwargs else "--personal"
        # keeping it simple, will add more parameters later
    def generate(self, result, keywords, keynums):
        doname(self.name, self.mode, result, keywords, keynums)
        print("generating all name permutations...")
