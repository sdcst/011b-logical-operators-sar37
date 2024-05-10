#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
question = " enter a number"
n = input(question)
n = int(n)
nn = "enter another number"
nn = input(nn)
nn = int(nn)
if n >= nn:
    print(f"{n} is bigger than {nn}")
    f = n/nn
    f = round(f)
    if n/f == nn:
        print(f"{nn} is a factor of {n}")
elif nn >= nn:
    print(f"{n} is smaller than {nn}")
    f = nn/n
    f = round(f)
    if nn/f == n:
        print(f"{nn} is a factor of {n}")
elif n == nn:
    print(f"{n} and {nn} are equal")
    print(f"{n} is a factor of{nn}")






