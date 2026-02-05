# creating a programme that's going to check how many numbers in an array are even or odds
# first we going to declare two variables a and b to store the even and odds numbers.
# second we going to predefine an array of ten elements, and then we going to use a for 
# loop that  will go through all the array and returns the amount of numbers that are even 
# or odds and will store those values in a, b, and print the message on the first 
# line "the even numbers in this array are: a" 
# and then on the second line "the odds numbers in this array are: b"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = []
b = []
for num in numbers:
    if num % 2 == 0:
        # a = the even numbers 
        a.append(num)

    else:
        # b = the odds numbers
        b.append(num)
print("the even numbers in this array are:", a)
print("the odds numbers in this array are:", b)
     