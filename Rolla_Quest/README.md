# ROLLA QUEST

## Introduction
In the 21st century, when cheetos and video games rule the earth, there lives a determined
student who, against all obstacles, will get to class on time. He or she will be faced with
many challenges, some of which will be students asking for directions to their classrooms, 
mothers trying to hug them, sweater vendors trying to sell St. Pats sweaters, and brother 
Jed trying to preach the gospel to them. This quest will be held on the MST Campus in Rolla 
Missouri. As they say every story has a beginnig, and some beginnings are better than others. 

![](st_pats.png)

## Goal
The goal of this assignment is to give our character the ability to move around the MST Campus and
to be able to enter and leave the CS Building. This will require you to make changes to the 
code that's being provided to you. 

In this assignment there will be 4 functions that you'll have to define: `make_move()`, 
`go_inside_cs_building()`, `go_outside_cs_building()`, and `is_valid_move()`. With these 
4 functions defined, your character should be able to move around campus maps, and roam all 
three floors of the CS building. This assignment will prepare you for the next assignment 
where you'll interact with other characters in the game such as brother Jed, the hugging moms, 
and St. Pats Sweater Vendors!  

## Special Characters on the maps
`^` this is found inside and outside the cs building and represents entering/leaving the building

`+` this is found inside the cs building and represents the stairwells that lead to a upper level floor

`-` this is found inside the cs building and represents the stairwells that lead to a lower level floor

## Files That Are Provided

### Game Maps
* `maps/cs_first_floor.txt`
* `maps/cs_second_floor.txt`
* `maps/cs_third_floor.txt`

### Rolla Quest Code
* `rolla_quest.py`
* `game_utilites.py`

### Unit Tests
* `run_tests.sh` Note: actually run this on your computer, for more efficient testing.
* `unit_tests/*`

# Reminders
When your gitlab CI jobs are green/passing, you're good!
If your gitlab CI jobs are red/failing, you have issues.

If are having a problem with a particular unit test, trace the unit test in debug mode:
```sh
cd unit_tests
pudb3 testofinterest.py
# or
spyder3 testofinterest.py
```

