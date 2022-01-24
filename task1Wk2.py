from typing import DefaultDict


slow = 0
medium = 0
fast = 0
time = int(input("enter a number: "))
while time != 0:
    if time < 30:
        fast = fast + 1
    elif time < 60: 
        medium = medium + 1
    else:
        slow = slow + 1   
    time = int(input("enter a number: "))


print(slow, medium, fast)