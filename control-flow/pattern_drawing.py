size = int(input("Enter the size of the pattern: "))
fixed_size = size

while size > 0:
    for i in range(1, fixed_size + 1):
        print("*", end=" ")
    size -= 1
    print()
    
