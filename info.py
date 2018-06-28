from functions import * 

class Info: 
    def __init__(self, **kwargs): 
        if "mode" not in kwargs: 
            raise AttributeError("[!] mode required")
        self.name = kwargs["name"] if "name" in kwargs else None 
        self.currentyear = kwargs["currentyear"] if "currentyear" in kwargs else None 
        self.address = kwargs["address"] if "address" in kwargs else None 
        self.aliases = kwargs["aliases"] if "aliases" in kwargs else None
        self.motto = kwargs["motto"] if "motto" in kwargs else None 
        self.phone = kwargs["phone"] if "phone" in kwargs else None 
        self.dob = kwargs["dob"] if "dob" in kwargs else None
        self.email = kwargs["email"] if "email" in kwargs else None 
        self.family = kwargs["family"] if "family" in kwargs else None 
        self.mode = kwargs["mode"]
        # keeping it simple, will add more parameters later
    def generate(self, result, keywords, keynums, pooltxt):
        doname(self.name, self.mode, result, keywords, keynums, pooltxt) 
        doemail(self.email, self.mode, result, keywords, keynums, pooltxt) 
        dophone(self.phone, self.mode, result, keywords, keynums, pooltxt)
        if self.mode == "--enterprise":
            if self.address:
                doaddress(self.address, self.mode, result, keywords, keynums, pooltxt) 
        if self.mode == "--personal":
            doaliases(self.aliases, self.mode, result, keywords, keynums, pooltxt)
            #dofamily(self.family, self.mode, result, keywords, keynums, pooltxt)
            #dodob(self.dob, self.mode, result, keywords, keynums, pooltxt) 
        permutations(result, keywords, keynums, pooltxt)
