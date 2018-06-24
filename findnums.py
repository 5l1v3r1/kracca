import itertools
import threading
import time
import sys 
import re

# simple tool that retrieves all numbers used in passwords from a database dump, written by lolcow for kracca

done = False

def animate():
    global done
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rreading... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!\n ')

def main():
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")
    t = threading.Thread(target=animate)
    t.start()
    line = infile.readline()
    while line:
        if any(char.isdigit() for char in line):
                z = line.split("@")
                out = z[-1]
                out = re.sub('[^0-9]','',line)
                outfile.write(out + "\n") 
                line = infile.readline()
        else: 
            line = infile.readline() 
            pass
    global done
    done = True
    infile.close() 
    outfile.close()

main()
