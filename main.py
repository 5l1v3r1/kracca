from pyfiglet import Figlet 
from info import Info 
import sys

def main(): 
    f = Figlet(font='slant')
    print(f.renderText('kracca'))
    print("by six & lolcow")
    if sys.argv[1] == "--enterprise": 
        print("====ENTERPRISE MODE====")
    elif sys.argv[1] == "--personal": 
        print("====PERSONAL MODE====")
    keynums = input("keynum file: ")
    keywords = input("keyword file: ")
    results = input("result file: ") 
    i = Info(name=input("name: "), currentyear=input("current year: "), address=input("address: "), motto=input("motto: "), phone=input("phone: "), dob=input("dob: "), email=input("email: "), family=input("family: "), mode=sys.argv[1])
    print("generating passwords....")
    print(i.name) 
    print(i.currentyear) 
    print(i.address) 

    i.generate(results, keywords, keynums)
    
main()
