from pyfiglet import Figlet 
from info import Info
import sys

def hlp(): 
    print("usage: python main.py results.txt keywords.txt keynums.txt pooltext.txt\n--enterprise     enterprise mode\n--personal     personal mode\n--caps-only     filters output for passwords that contain only capital letters\n--with-nums     filters output for passwords that contain numbers")

def main(): 
    f = Figlet(font='slant')
    print(f.renderText('kracca'))
    if len(sys.argv) == 1:
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
    if len(sys.argv) == 6: 
        result  = sys.argv[2] 
        keywords = sys.argv[3] 
        keynums = sys.argv[4]
        pooltxt = sys.argv[5]
        if sys.argv[1] == "--enterprise": 
            i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise")
        elif sys.argv[1] == "--personal":
            i = Info(name=input("name: "), aliases=input("aliases: "),address=input("address: "), phone=input("phone: "), email=input("emails: "), family=input("family names: "), mode="--personal")
    elif len(sys.argv) == 7:
        result  = sys.argv[2] 
        keywords = sys.argv[3] 
        keynums = sys.argv[4]
        pooltxt = sys.argv[5]
        filter1 = sys.argv[6]
        if filter1 == "--caps-only":
            if sys.argv[1] == "--enterprise": 
                i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise", capitalfilter=filter1 )
            elif sys.argv[1] == "--personal":
                i = Info(name=input("name: "), aliases=input("aliases: "),address=input("address: "), phone=input("phone: "), email=input("emails: "), family=input("family names: "), mode="--personal", capitalfilter=filter1)
        elif filter1 == "--with-nums": 
            if sys.argv[1] == "--enterprise": 
                i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise", numberfilter=filter1)
            elif sys.argv[1] == "--personal":
                i = Info(name=input("name: "), aliases=input("aliases: "),address=input("address: "), phone=input("phone: "), email=input("emails: "), family=input("family names: "), mode="--personal", numberfilter=filter1) 
    elif len(sys.argv) == 8: 
        result  = sys.argv[2] 
        keywords = sys.argv[3] 
        keynums = sys.argv[4]
        pooltxt = sys.argv[5]
        filter1 = sys.argv[6]
        filter2 = sys.argv[7]
        if filter1 == "--caps-only":
            if sys.argv[1] == "--enterprise": 
                i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise", capitalfilter=filter1, numberfilter=filter2)
            elif sys.argv[1] == "--personal":
                i = Info(name=input("name: "), aliases=input("aliases: "),address=input("address: "), phone=input("phone: "), email=input("emails: "), family=input("family names: "), mode="--personal", capitalfilter=filter1, numberfilter=filter2)
        elif filter1 == "--with-nums": 
            if sys.argv[1] == "--enterprise": 
                i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), email=input("email: "), mode="--enterprise", numberfilter=filter1, capitalfilter=filter2)
            elif sys.argv[1] == "--personal":
                i = Info(name=input("name: "), aliases=input("aliases: "),address=input("address: "), phone=input("phone: "), email=input("emails: "), family=input("family names: "), mode="--personal", numberfilter=filter1, capitalfilter=filter2) 
    print("bl1ng bl1ng i c u ;)")
    i.generate(result, keywords, keynums, pooltxt)
    
main()
