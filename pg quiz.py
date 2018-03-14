import pyautogui as pg
import time

points = 0

# Question
answer = pg.prompt(
"""
wich would you rather do?

a) play video games
b) do homework
""")
if answer == "a":
    points += 3
elif answer == b:
    points += 0

answer = pg.prompt(
"""
wich would you rather do?

a) play hockey
b) play football
""")
if answer == "a":
    points += 3
elif answer == b:
    points += 0

answer = pg.prompt(
"""
wich would you rather do?

a) go sky diving
b) go bunji jumping
""")
if answer == "a":
    points += 3
elif answer == b:
    points += 0

pg.alert ("you are cool")
