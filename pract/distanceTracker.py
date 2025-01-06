# You are writing a program to help track distances for a running app. Your program should:

# Accept the distance you ran today in kilometers as input.
# Convert the distance to miles.
# Display the distance in miles.
# Use functions to organize your code, such as one function to perform the conversion and another to display the result. For example, if the user runs 5 kilometers, the program should calculate and display the equivalent distance in miles.

# (Hint: 1 kilometer = 0.621371 miles)

distance_ran = float(input("Enter the distance you ran today in kilometers: "))

def kilometer_to_mile(kilometer):
    miles = kilometer * 0.621371
    return miles

distance_miles = kilometer_to_mile(distance_ran)

print(distance_miles)