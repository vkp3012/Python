""" 
ABC is a right triangle, 90°  at .
Therefore, angle ABC=90°.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC (angle 0° , as shown in the figure) in degrees.
"""


import math
AB,BC = int(input()),int(input())
hypo = math.hypot(AB,BC)
res = round(math.degrees(math.acos(BC/hypo)))
degree = chr(176)
print(res,degree,sep='')