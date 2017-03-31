def main():
    n=int(raw_input())
    if(n>0):
        cr=int(n**(1.0/3.0))
    else:
        cr=int((-n)**(1.0/3.0))
    print cr


main()

