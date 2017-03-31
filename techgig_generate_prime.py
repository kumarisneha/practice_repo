def main():
    r1=int(raw_input())
    r2=int(raw_input())
    count =0
    for i in range(r1,r2+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print i           

main()
