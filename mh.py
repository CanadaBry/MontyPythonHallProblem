from random import randint, random, seed

def simulate() -> bool:
    doors: list = [1,2,3] # Our 3 doors

    car: int = randint(1,3) # Pick one at random to have the car in it
    door: int = randint(1,3) # Player picks one door at random

    doors.remove(door) # Remove the players door from available doors

    # Remove an available door
    if car in doors: # Host cannot open door with car in it
        doors = [car] # Remove door without the car
    else: # Player's door is the car
        doors.pop(randint(0,1)) # Remove either door
    
    switch: int = doors[0] # The door the player has the option to switch with

    won: bool = switch == car # Does the player win if they switch?

    return won

def simulateSimplified() -> bool:
    # Pick Car Door and Player Door
    car: int = randint(1,3)
    door: int = randint(1,3)

    # Below is the simplified logic from the above function:
    # 'if car in doors' can be changed to 'if car != door'
    # body of can be 'switch = True' (implicitly you win if you switch to the car) -> can be simplified to 'return True'
    # You cannot win by switching if you picked the car, so 'else' can be simplified to 'return False'.
    # pattern is: 'if car != door: return True; else: return False;' -> this can be simplified to 'return car != door'
    return car != door 

def simulateSimplifiedFurther() -> bool:
    # chance of 'car != door' = 1 - chance of 'car == door'
    # 'car == door' -> 'randint(1,3) == randint(1,3)'
    # break into cases for first chosen randint(1,3): 'randint(1,3) == randint(1,3)' -> '1 == randint(1,3)', '2 == randint(1,3)', '3 == randint(1,3)'
    # No matter what is chosen for first randint(1,3) the chance is 1/3 the statement is True
    # using initial statement 'car != door' = 1 - 'car == door' -> 1 - 1/3 = 2/3
    return random() < 2/3
    

def run(simulateFunc: callable, n: int, fixedSeeds: bool = False) -> float:
    wins: int = 0
    runs: int = 0
    while runs < n:
        if fixedSeeds: seed(runs) # Used to show simulate and simualteSimplified are the same
        outcome: bool = simulateFunc()
        if outcome:
            wins +=1
        runs += 1
    return wins/n

if __name__ == '__main__':
    useFixedSeeds: bool = True
    numRuns: int = 100000
    print(f'Simulate:            {run(simulate, numRuns, useFixedSeeds)}')
    print(f'Simulate Simplified: {run(simulateSimplified, numRuns, useFixedSeeds)}')