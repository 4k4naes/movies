from ranks.filmweb import get_dataF
from ranks.IMDb import get_dataI

pages = ["filmweb", "IMDb"]

def main():
    print("Wybierz stronę:\n1. filmweb\n2. IMDb")
    option = int(input())

    if(option == 1):
        get_dataF()
    elif(option == 2):
        get_dataI()
    else:
        print("nieistniejąca opcja")
    

if __name__ == "__main__":
    main()