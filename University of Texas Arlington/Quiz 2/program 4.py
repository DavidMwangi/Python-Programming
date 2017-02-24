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

while end ==0:
    
    time = input("Please enter time in seconds:\n")

    if int(time) < 3600:

        days = 0

        minutes = int(time)//60

        seconds = int(time)%60

        hours = 0

        output = ("%s days %s hours %s minutes %s seconds\n")

        print (output %(days, hours, minutes, seconds))

        end = 0

    elif int(time) >= 3600 and int(time)<86400:

        days = 0

        hours = int(time) // 3600

        if int(time) % 3600 >= 60:

            minutes = int(int(time)%3600//60)

            seconds = int(int(time)%3600%60)

        output = ("%s days %s hours %s minutes %s seconds\n")

        print (output %(days, hours, minutes, seconds))

        end = 0

    """"elif int(time)>=86400:

        days = int(time)//86400

        if int(time)%86400 >= 3600:

            hours = int(time)%86400 // 3600

            if (int(time)%86400) % 3600 >= 60:

                minutes = int(int(time)%86400) % 3600 // 60

                seconds = int(int(time)%86400) % 3600 % 60

        
        output = ("%s days %s hours %s minutes %s seconds\n")

        print (output %(days, hours, minutes, seconds))""""
    else:

        end =1
    
