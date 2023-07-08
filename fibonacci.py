a = int(input("enter terms"))

n1=0
n2=1

sum =0

if a<=0:
    print("enter a +ve integer")
else:
    for i in range(0,a):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1 + n2

        # n1 = n2
        # n2 = sum
        # sum = n1 + n2
