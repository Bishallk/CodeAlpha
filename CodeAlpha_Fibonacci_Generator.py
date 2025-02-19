
# #-The Fibonacci series is a sequence where each number is the sum of the two preceding numbers, defined by a mathematical recurrence relationship.


def fibo_generator():
    n=int(input("Enter Number of Fibonacci : ")) #taking input from users.
    series=[] #list to store fibonacci series
    if(n<0):
        print("Please Enter Positive Number.")
    else:
        a,b=0,1
        for _ in range(n):
            series.append(a) #adding new fibonacci to list
            a,b=b,a+b
        
    return series

print(fibo_generator())