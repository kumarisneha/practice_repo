def main():
    n=int(raw_input())
    f1=0
    f2=1 
    print f1,f2,
    for i in range(2,n):
        temp=f1 
        f1=f2
        f2=f1+temp
        print f2, 
            

main()
