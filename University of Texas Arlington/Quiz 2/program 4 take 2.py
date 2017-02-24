"""

Write a program that asks the user to enter a positive integer n.
Assuming that this integer is in seconds, your program should convert the number of seconds into days,
hours, minutes, and seconds and prints them exactly in the format specified below.
Here are a few sample runs of what your program is supposed to do: 

when user enters

369121517
your program should print:
4272 days 5 hours 45 minutes 17 seconds
when user enters
24680
your program should print:
0 days 6 hours 51 minutes 20 seconds
when user enters
129600
your program should print:
1 days 12 hours 0 minutes 0 seconds


"""

end = 0

while end == 0:

    
    number = int(input("Please enter your input:\n"))

    days = number // 86400

    days_rem = number % 86400

    hours = days_rem // 3600

    hours_rem = days_rem % 3600

    minutes = hours_rem // 60

    seconds = hours_rem % 60

    output = ("%s days %s hours %s minutes %s seconds")

    print(output %(days, hours, minutes, seconds))

