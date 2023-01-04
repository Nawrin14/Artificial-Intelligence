#Define a recursive procedure to find the sum of 1st n terms of an equal-interval series given the 1st term and the interval

def rec_sum(i,j,s):
    if i==num:
        return s
    else:
        j+=interval
        s+=j
        return rec_sum(i+1,j,s)

firstTerm=int(input("Enter the 1st term: "))
interval=int(input("Enter the interval: "))
num=int(input("Enter number of terms: "))

sum=firstTerm
i=1
j=firstTerm

if num<=0:
    print("The number of terms must be positive.")
else:    
    print("The sum is: ",rec_sum(i,j,sum))
