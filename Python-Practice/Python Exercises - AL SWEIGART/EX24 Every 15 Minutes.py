"""
Exercise Description
    Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm.
Your solution should produce the following output:
12:00 am
12:15 am
12:30 am
12:45 am
1:00 am
1:15 am
--cut--
11:30 pm
11:45 pm
There are 96 lines in the full output.
"""

def printevery15mins():
    for i in range(2):
        for j in range(12):
            time = "am" if i == 0 else "pm"
            if j == 0:
                j = 12
                print(f"{j}:00 {time}")
                print(f"{j}:15 {time}")
                print(f"{j}:30 {time}")
                print(f"{j}:45 {time}")
            else:
                print(f"{j}:00 {time}")
                print(f"{j}:15 {time}")
                print(f"{j}:30 {time}")
                print(f"{j}:45 {time}")
                
printevery15mins()

# the code given by chat gpt is again way smarter that me
# def printevery15mins():
#     for hour in range(24):
#         period = 'am' if hour < 12 else 'pm'
#         display_hour = hour % 12
#         if display_hour == 0:
#             display_hour = 12
#         for minute in [0, 15, 30, 45]:
#             print(f"{display_hour}:{minute:02d} {period}")

# printevery15mins()
