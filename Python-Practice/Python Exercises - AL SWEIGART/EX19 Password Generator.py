"""
Exercise Description
    Write a generatePassword() function that has a length parameter. The length
parameter is an integer of how many characters the generated password should have. For security
reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway. The password
string returned by the function must have at least one lowercase letter, one uppercase letter, one
number, and one special character. The special characters for this exercise are ~!@#$%^&*()_+.
Your solution should import Python's random module to help randomly generate these
passwords.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:

assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in "abcdefghijklmnopqrstuvwxyz":
        hasLowercase = True
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
        hasUppercase = True
    if character in "1234567890":
        hasNumber = True
    if character in "~!@#$%^&*()_+":
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
"""

import random
def generatePassword(length):
    if length < 12:
        length = 12
    
    special_chars = "~!@#$%^&*()_+"
    pwd = ""
    while len(pwd) <= length:
        upper_alphabets = chr(random.randint(65, 90))
        lower_alphabets = chr(random.randint(97, 122))
        pwd += (f"{upper_alphabets}{special_chars[random.randint(0,12)]}{lower_alphabets}{random.randint(0,9)}")
    return pwd[:length]

assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in "abcdefghijklmnopqrstuvwxyz":
        hasLowercase = True
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
        hasUppercase = True
    if character in "1234567890":
        hasNumber = True
    if character in "~!@#$%^&*()_+":
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial


# =======================================
# chat gpt's version way smarter than me 
# =======================================


# import random

# LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
# UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# NUMBERS = '0123456789'
# SPECIAL = '~!@#$%^&*()_+'

# def generatePassword(length):
#     if length < 12:
#         length = 12

#     # Step 1: guarantee at least one char from each category
#     password_chars = [
#         random.choice(LOWER_LETTERS),
#         random.choice(UPPER_LETTERS),
#         random.choice(NUMBERS),
#         random.choice(SPECIAL)
#     ]

#     # Step 2: fill the rest
#     all_chars = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
#     remaining_length = length - 4
#     password_chars += random.choices(all_chars, k=remaining_length)

#     # Step 3: shuffle to randomize positions
#     random.shuffle(password_chars)

#     # Step 4: join to string and return
#     return ''.join(password_chars)

# # ✅ Tests (copy-paste directly under your function)
# assert len(generatePassword(8)) == 12

# pw = generatePassword(14)
# assert len(pw) == 14
# hasLowercase = any(c in LOWER_LETTERS for c in pw)
# hasUppercase = any(c in UPPER_LETTERS for c in pw)
# hasNumber = any(c in NUMBERS for c in pw)
# hasSpecial = any(c in SPECIAL for c in pw)
# assert hasLowercase and hasUppercase and hasNumber and hasSpecial


