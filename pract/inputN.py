# Given an input n
# print out a triangle
# of height n

def print_triangle(n):
    for i in range(1, n+1):
        print("*" * i)

print_triangle(6)