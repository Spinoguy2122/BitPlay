def rightmost_set_bit_position(n):
    if n == 0:
        return 0   

 
    rightmost_bit = n & (-n)

   
    position = 1
    while rightmost_bit > 1:
        rightmost_bit >>= 1
        position += 1

    return position



n = int(input("Enter number: "))


pos = rightmost_set_bit_position(n)
print("Position of the first set bit:", pos)
