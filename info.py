from functions import * 

class Info: 
    def __init__(self, **kwargs): 
        if "mode" not in kwargs: 
            raise AttributeError("[!] mode required")
        self.name = kwargs["name"] if "name" in kwargs else None 
        self.currentyear = kwargs["currentyear"] if "currentyear" in kwargs else None 
        self.address = kwargs["address"] if "address" in kwargs else None 
        self.motto = kwargs["motto"] if "motto" in kwargs else None 
        self.phone = kwargs["phone"] if "phone" in kwargs else None 
        self.dob = kwargs["dob"] if "dob" in kwargs else None
        self.email = kwargs["email"] if "email" in kwargs else None 
        self.family = kwargs["family"] if "family" in kwargs else None 
        self.mode = kwargs["mode"]
        # keeping it simple, will add more parameters later
    def generate(self, result, keywords, keynums):
        
        # only name and email permutations are supported ATM, either me or six will add more functionality soon 
        # the amount of factors that go into generating a plausible password is actually insane
        # i don't think i've ever done this much math in my life and i have dyscalculia - lolcow

        if self.name: 
            doname(self.name, self.mode, result, keywords, keynums) 
        if self.email: 
            doemail(self.email, self.mode, result, keywords, keynums)

