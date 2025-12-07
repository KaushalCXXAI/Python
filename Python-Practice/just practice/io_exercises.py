def exercise1():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    ans = a * b
    print(f"product of {a} and {b} is {ans}")

# exercise1()

def exercise2():
    str1 = 'My'
    str2 = 'Name'
    str3 = 'Is'
    str4 = 'James'
    print(str1, str2, str3, str4,sep="**")

# exercise2()

def exercise3():
    num = 10
    print(format(num, 'o'))
    print(oct(num))
    print('%o' % num)
    print(f"{num:o}")

# exercise3()

def exercise4():
    num = 458.541315
    print('%.2f' % num)

# exercise4()

def exercise5():
    my_list = []
    for i in range(1,6):
        my_list.append(int(input(f"Enter Number{i} : ")))
    print(my_list)

# exercise5()

def exercise6():
   pass
