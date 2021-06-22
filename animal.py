import sys
def default():
    print("Hello")

def cati():
    print("Meaowww")

def dog():
    print("Bhaoww")

def lion():
    print("Roarr")
def main():
    if sys.argv[1]=="cat":
        cati()
    elif sys.argv[1]=="lion":
        dog()
    elif sys.argv[1]=="lion":
        lion()
    else:
        default()

if __name__=="__main__":
    main()
