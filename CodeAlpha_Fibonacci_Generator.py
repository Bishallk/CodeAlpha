
# #-The Fibonacci series is a sequence where each number is the sum of the two preceding numbers, defined by a mathematical recurrence relationship.


def get_input():
    return int(input("Enter Number of Fibonacci : ")) #taking input from users.

def fibo_generator():
    n=get_input()
    series=[] #list to store fibonacci series
    if(n<0):
        print("Please Enter Positive Number.")
        return
    else:
        a,b=0,1
        for _ in range(n):
            series.append(a) #adding new fibonacci to list
            a,b=b,a+b
    return series #returns list of fibonacci series

print("Normal: ",fibo_generator())


#using Generator / yield keyword
def fibonacci():
    n=get_input()
    if(n>0):
        a,b=0,1
        for _ in range(n):
            yield a
            a,b=b,a+b
    else:
        print("Please Enter Positive Number")
        return

series= fibonacci()
print("using generator")
for i in series:
    print(i)


