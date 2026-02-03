import math

name = input()
episode = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

free_time = break_time - lunch_time - rest_time

if free_time >= episode:
    leftover = math.ceil(free_time - episode)
    print(f"You have enough time to watch {name} and left with {leftover} minutes free time.")
else:
    needed = math.ceil(episode - free_time)
    print(f"You don't have enough time to watch {name}, you need {needed} more minutes.")
