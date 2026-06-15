# ================================
# BITWISE SWAP CHALLENGE
# ================================

print("================================")
print("BITWISE SWAP CHALLENGE")
print("================================")


# ------------------------------------------------
# STEP 1: SWAP WITHOUT A THIRD VARIABLE
# ------------------------------------------------

a = 56
b = 12

print("\nStep 1: Swap Without a Third Variable")
print("Before Swap:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After Swap:")
print("a =", a)
print("b =", b)


# ------------------------------------------------
# STEP 2: PERFORM XOR SWAP
# ------------------------------------------------

x = 45
y = 18

print("\nStep 2: Perform XOR Swap")
print("Before XOR Swap:")
print("x =", x)
print("y =", y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After XOR Swap:")
print("x =", x)
print("y =", y)


# ------------------------------------------------
# STEP 3: USE LEFT SHIFT TO DOUBLE NUMBERS
# ------------------------------------------------

number = 3

print("\nStep 3: Use Left Shift to Double Numbers")
print("Original Number:", number)

print(number, "<< 1 =", number << 1)
print(number, "<< 2 =", number << 2)
print(number, "<< 3 =", number << 3)
print(number, "<< 4 =", number << 4)

print("Each left shift multiplies the number by 2.")


# ------------------------------------------------
# STEP 4: DETECT DIFFERENT SIGNS WITH XOR
# ------------------------------------------------

num1 = -10
num2 = 5

print("\nStep 4: Detect Different Signs with XOR")
print("num1 =", num1)
print("num2 =", num2)

if (num1 < 0) ^ (num2 < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")


# ------------------------------------------------
# STEP 5: DIVIDE WITHOUT USING /
# ------------------------------------------------

dividend = 25
divisor = 4

quotient = 0
remainder = dividend

while remainder >= divisor:
    remainder = remainder - divisor
    quotient = quotient + 1

print("\nStep 5: Divide Without Using /")
print("Dividend:", dividend)
print("Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)


# ------------------------------------------------
# STEP 6: RUN AND TEST THE PROGRAM
# ------------------------------------------------

print("\nStep 6: Run and Test the Program")
print("Program executed successfully.")
print("Try changing the numbers to test more cases.")


# FINAL SUMMARY

print("\n================================")
print("BITWISE SWAP CHALLENGE SUMMARY")
print("================================")
print("Swap without third variable uses + and -")
print("XOR swap uses the ^ operator")
print("Left shift doubles numbers")
print("XOR detects different signs")
print("Division uses repeated subtraction")
print("================================")