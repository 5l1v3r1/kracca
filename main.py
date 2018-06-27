from pyfiglet import Figlet 
from info import Info 
import sys

def main(): 
    f = Figlet(font='slant')
    print(f.renderText('kracca'))
    print("by six & lolcow")
    if len(sys.argv) == 0:
        print("must provide mode:\n--enterprise:    includes address and differing name permutations in results\n--personal:    includes DOB and family permutations")
    else: 
        if sys.argv[1] == "--enterprise": 
            print("====ENTERPRISE MODE====")
        elif sys.argv[1] == "--personal": 
            print("====PERSONAL MODE====")
        if sys.argv[1] == "--help": 
            print("--enterprise\n--personal\nformat: results.txt keywords.txt keynums.txt pooltxt.txt")
            exit()
        result  = sys.argv[2] 
        keywords = sys.argv[3] 
        keynums = sys.argv[4]
        pooltxt = sys.argv[5]
    if sys.argv[1] == "--enterprise": 
        i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise")
    elif sys.argv[1] == "--personal":
        i = Info(name=input("name: "), address=input("address: "), phone=input("phone: "), email=input("email: "), mode="--personal")
    print("generating passwords....")
    print(i.name) 
    print(i.currentyear) 
    print(i.address) 
    i.generate(result, keywords, keynums, pooltxt)
    
main()
