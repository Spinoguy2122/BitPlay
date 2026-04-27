def reverse_bits(n):
    rev = 0
    while n > 0:
        rev = (rev << 1) | (n & 1) 
        n = n >> 1                  
    return rev


num = int(input("Enter your original number: "))

reversed_num = reverse_bits(num)


print(f"Original Number: {num} ({bin(num)[2:]})")
print(f"Reversed Number: {reversed_num} ({bin(reversed_num)[2:]})")