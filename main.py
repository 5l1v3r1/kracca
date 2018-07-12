from pyfiglet import Figlet 
from info import Info 
import sys

def hlp(): 
    print("--enterprise     enterprise mode\n--personal     personal mode\n--caps-only     filters output for passwords that contain only capital letters\n--with-nums     filters output for passwords that contain numbers")


def main(): 
    f = Figlet(font='slant')
    print(f.renderText('kracca'))
    if len(sys.argv) == 0:
        print("must provide mode:\n--enterprise:    includes address and differing name permutations in results\n--personal:    includes DOB and family permutations")
        exit()
    elif len(sys.argv) != 6: 
        hlp()
        exit()
    else: 
        if sys.argv[1] == "--enterprise": 
            print("====ENTERPRISE MODE====")
        elif sys.argv[1] == "--personal": 
            print("====PERSONAL MODE====")
        if sys.argv[1] == "--help": 
            hlp()
            exit()
        result  = sys.argv[2] 
        keywords = sys.argv[3] 
        keynums = sys.argv[4]
        pooltxt = sys.argv[5]
    if sys.argv[1] == "--enterprise": 
        i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise")
    elif sys.argv[1] == "--personal":
        i = Info(name=input("name: "), aliases=input("aliases: "),address=input("address: "), phone=input("phone: "), email=input("emails: "), family=input("family names: "), mode="--personal")
    print("bl1ng bl1ng i c u ;)")
    i.generate(result, keywords, keynums, pooltxt)
    
main()
