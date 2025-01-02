
#!usr/bin/python3
import sys

def repeat(s, exclaim):
    
    result = s + s + s 

    if exclaim:
        result = result + '!!!'
    return result

if __name__ == '__main__':
    value = True if sys.argv[2].lower() == "true" else False
    print(repeat(sys.argv[1],value))


