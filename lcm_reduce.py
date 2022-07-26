from numpy import random
import numpy as np

user = int(input("enter a number:"))
number2 = int(input("How many numbers should be 'randomized' >>> "))
a = random.randint(2, user)
b = np.arange(a, number2)
x = np.lcm.reduce(b)

if number2 < a:
  g = input(f"\n\nSorry, the number {number2} you entered is less than the 'random' number! So please 'run' again")
else:
  print(f"The number you entered has been randomized to {user} and this number!Randomized number\n[{a}] \n\nAgain, the {number2} you entered is 'ranged' from the random random number you entered to the [<{number2}>] you entered \n{b}.\n\nAnd the lowest common multiple of these numbers\n{x}")