#Project 1: Password Strength Checker
# Password Strength Checker


password = input("Enter a password: ")

#set up flags
has_upper = False
has_digit = False
has_symbol = False
symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

#check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True
    if char in symbols:
        has_symbol = True

#check the length of the password
if len(password) < 8:
    is_long_enough = False
else:
    is_long_enough = True

#check if all criteria are met
score = 0
if is_long_enough:
    score += 1
if has_upper:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

#output the strength of the password
print("\n--- Password Strength Checker ---")
if is_long_enough:
    print("Length (8+):          PASS")
else:
    print("Length (8+):          FAIL")
if has_upper:
    print("Contains Uppercase:   PASS")
else:
    print("Contains Uppercase:   FAIL")
if has_digit:
    print("Contains Digit:       PASS")
else:    print("Contains Digit:       FAIL")
if has_symbol:
    print("Contains Symbol:      PASS")
else:   
    print("Contains Symbol:      FAIL")

    #final verdict
print("\nYour Score:", score, "out of 4")
if score <=1:
    print("Password Strength: WEAK")
elif score == 2:
    print("Password Strength: MEDIUM")
elif score == 3:
    print("Password Strength: MEDIUM-STRONG")
else:
    print("Password Strength: STRONG")

print("---------------------------------------")