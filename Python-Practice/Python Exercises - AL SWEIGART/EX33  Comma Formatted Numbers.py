"""
Write a commaFormat() function with a number parameter. The argument for this parameter 
can be an integer or floating-point number. Your function returns a string of this number with proper 
US/UK comma formatting. There is a comma after every third digit in the whole number part. There 
are no commas at all in the fractional part: The proper comma formatting of 1234.5678 is 1,234.5678 
and not 1,234.567,8.  
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statement's 
conditions are all True:
"""
def commaFormat(number):
    
    ans = ""
    original = str(number)
    number = original
    after_dot = ""
    if len(number) <= 3:
        return str(number)
    
    if "." in number:
        after_dot += "." + original.split(".")[1]
        if len(number) <= 3:
            return str(number)
      
    number = number.split(".")[0]
    commas = int(len(number) / 3)
    
    number = list(number)
    number.reverse()
    index = 3
    if int(len(number) % 3) == 0:
        commas -= 1
        
        
    for i in range(commas):
        number.insert(index,",")
        index =index + number.index(",") + 1
    number.reverse()
    ans ="".join(number)
    ans += after_dot
   
        
    print(ans)
    return str(ans)
    

commaFormat(1002423435230.123456)
    
    
    
assert commaFormat(1) == '1' 
assert commaFormat(10) == '10' 
assert commaFormat(100) == '100' 
assert commaFormat(1000) == '1,000' 
assert commaFormat(10000) == '10,000' 
assert commaFormat(100000) == '100,000' 
assert commaFormat(1000000) == '1,000,000' 
assert commaFormat(1234567890) == '1,234,567,890' 
assert commaFormat(1000.123456) == '1,000.123456' 


# # the simple version 
# def commaFormat(number):
#     print(f"{number:,}")
#     return f"{number:,}"

# chat gpt version

def commaFormat(number):
    s = str(number)

    # Separate integer and decimal parts
    if "." in s:
        integer, decimal = s.split(".")
        decimal = "." + decimal
    else:
        integer, decimal = s, ""

    # If short, no need to format
    if len(integer) <= 3:
        return integer + decimal

    # Build formatted string from the right
    rev = integer[::-1]
    parts = [rev[i:i+3] for i in range(0, len(rev), 3)]
    formatted = ",".join(parts)[::-1]

    return formatted + decimal
