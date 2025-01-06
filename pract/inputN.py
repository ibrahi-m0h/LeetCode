# Given an input n
# print out a triangle
# of height n

def print_triangle(n):
    for num in range(1, n+1):
        print("*" * num)


print_triangle(5)