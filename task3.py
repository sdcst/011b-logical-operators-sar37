#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""

question = "enter a number"
n = input(question)
n = float(n)
i =round(n)

if n > 0 and i ==n:
    print(f"{n}that is a positive interger")
else:
    print(f"{n}that is not a positive interger")

