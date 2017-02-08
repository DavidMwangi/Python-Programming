"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,

find the sum of the even-valued terms.

"""

def fib(n):
    a, b = 1, 2
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

for i in range (fib(90)):
    sum = 0
    if i % 2 == 0:

        sum = sum + i
        i = i + 1

        print (sum)

    
