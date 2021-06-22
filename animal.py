import sys
def default():
    print("Hello")

def cat():
    print("Meaoww")

def dogi():
    print("Bhaoww")

def lion():
    print("Roarr")
def main():
    if sys.argv[1]=="cat":
        cat()
    elif sys.argv[1]=="lion":
        dogi()
    elif sys.argv[1]=="lion":
        lion()
    else:
        default()

if __name__=="__main__":
    main()
