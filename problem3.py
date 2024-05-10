#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
I = input(" enter an interger")
I = int(I)

II = input("enter a second interger")
II = int(II)

III = input("enter a thrid interger")
III = int(III)


ln = max(I,II,III)
print(ln)
ln = int(ln)

sn = min(I,II,III)
print(sn)
sn = int(sn)

mn = (ln**2) - (sn**2)

MN = mn**0.5
print(MN)
MN = int(MN)

if MN == I or MN == II or MN == III:
    print(f"{sn},{MN}, {ln} form a Pythagorean triple")
elif MN != I or MN != II or MN != III:
    print(f"{sn}, {MN}, {ln} do not form a Pythagorean triple")