# `Problem 1`: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
"""
Salary(Lakhs) : Tax(%)
*   Below 5 : 0%
*   5-10 : 10%
*   10-20 : 20%
*   above 20 : 30%
"""
salary = int(input("Enter your salary : "))
# HRA, DA, PF deduction
salary -= ((0.1 * salary) + (0.05 * salary) + (0.03 * salary))

if salary >= 500000 and salary < 1000000:
    salary -= (0.1 * salary)
elif salary < 2000000:
    salary -= (0.2 * salary)
else:
    salary -= (0.3 * salary)

print("Your in-hand salary : ", salary)

# `Problem 2`: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
angles = [float(input("Enter angle: ")) for _ in range(3)]
if angles[0] + angles[1] + angles[2] == 180:
    print("Triangle")
else:
    print("Not a triangle")

# `Problem 3`: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
cost_price = int(input("Cost Price : "))
selling_price = int(input("Selling Price : "))

print("Profit" if selling_price - cost_price > 0 else "loss")

# `Problem 4`: Write a menu-driven program -
"""
1. cm to ft
2. km to miles
3. USD to INR
4. exit
"""

choice = int(input(
    """
    Enter your choice
    1. cm to ft
    2. km to miles
    3. USD to INR
    4. exit
    """
))

if choice == 1:
    dist = int(input("Enter distance in cm : "))
    print(dist * 0.032)
elif choice == 2:
    dist = int(input("Enter distance in km : "))
    print(dist * 0.62)
elif choice == 3:
    price = int(input("Enter price in usd : "))
    print(price * 91)
else:
    print("exit")

# `Problem 5` - Exercise 12: Display Fibonacci series up to 10 terms - Lets use recursion to solve this problem
def fibonacci(n: int):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# `Problem 6` - Find the factorial of a given number using recursion
num = int(input("Enter the number : "))
def factorial(num: int):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(num))

# `Problem 7` - Reverse a given integer number.
num = int(input("Enter your number : "))
print(int(str(num)[::-1]))

"""### `Problem 8`: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.

**Example 1:**

`Input:`

```bash
30
```

`Output:`

```bash
276
```
"""

# Write code here

# `Problem 10`: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

for i in range(1000, 3001):
    # Fetching all the digits from current number
    curr_num = i
    status = True
    while curr_num != 0:
        digit = int(curr_num % 10)
        if(digit % 2 != 0): 
            status = False
            break
        curr_num /= 10
    if(status): print(i)

"""###`Problem 11`: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
!
```
> The numbers after the direction are steps.

> `!` means robot stop there.

**Please write a program to compute the distance from current position after a sequence of movement and original point.**

*If the distance is a float, then just print the nearest integer.*

Example:

`Input`:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
!
```
`Output`:
```
2
```
"""

# Write code here

"""###`Problem 12`:Write a program to print whether a given number is a prime number or not"""

# Write code here

"""###`Problem 13`:Print all the Armstrong numbers in a given range.
Range will be provided by the user<br>
Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
"""

# Write code here

"""###`Problem 14`:Calculate the angle between the hour hand and minute hand.

Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

Input:<br>
H = 9 , M = 0<br>
Output:<br>
90<br>
Explanation:<br>
The minimum angle between hour and minute
hand when the time is 9 is 90 degress.
"""

# Write code here

"""###`Problem 15`:Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

Note: It may be assumed that the rectangles are parallel to the coordinate axis.

<img src='https://www.geeksforgeeks.org/wp-content/uploads/rectanglesOverlap.png' width='300' height='200'>
"""

# input of 1st rectangle
x_lt_1 = int(input())
y_lt_1 = int(input())
x_rb_1 = int(input())
y_rb_1 = int(input())

x_lt_2 = int(input())
y_lt_2 = int(input())
x_rb_2 = int(input())
y_rb_2 = int(input())

# Checking right
if(x_rb_1 > x_rb_2 and y_rb_1 < y_rb_2): print("Overlap")
elif(x_rb_1 > x_rb_2 and y_rb_1 < y_rb_2): print("Overlap")