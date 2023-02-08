from random import randint, random, seed

def simulate() -> bool:
    doors: list = [1,2,3] # Represents the 3 doors

    car: int = randint(1,3) # Pick one door at random to have the car in it
    door: int = randint(1,3) # Player picks one door at random

    doors.remove(door) # Remove the players door from the available doors

    # Host removes an available door
    if car in doors: # Host cannot open door with car in it
        doors = [car] # So we remove the door without the car
    else: # Player's door is the car
        doors.pop(randint(0,1)) # Host can remove either door
    
    switch: int = doors[0] # Assign the door the player has the option to switch with

    won: bool = switch == car # Check if the player wins if they switch

    return won

def simulateSimplified() -> bool:
    # Pick Car Door and Player Door
    car: int = randint(1,3)
    door: int = randint(1,3)

    # Below is the simplified logic from the above function:
    # 1) The statements 'doors.remove(door)' and 'if car in doors' can be simplified to 'if car != door'
    # 2) Implicitly, you win if you switch to the car, so the body of the 'if' can simpified to 'won = True'. This can then be further simplified to 'return True'
    # 3) Similarily, you cannot win by switching if you picked the door with the car, so the 'else' can be simplified to 'return False'
    #
    # The pattern is now: 
    #
    # if car != door: 
    #   return True
    # else: 
    #   return False 
    #
    # This can be simplified to 'return car != door'

    return car != door 

def simulateSimplifiedFurther() -> bool:
    # Let's solve for the probability of 'car != door'
    # 1) Inverting the probability: Chance of 'car != door' = 1 - Chance of 'car == door'
    # 2) Replace the variables, with their values: 'car == door' -> 'randint(1,3) == randint(1,3)'
    # 3) Break the problem into cases based on value chosen in first randint(1,3): 'randint(1,3) == randint(1,3)' -> '1 == randint(1,3)', '2 == randint(1,3)', '3 == randint(1,3)'
    # 4) We can observe, no matter what is chosen for the first randint(1,3), the chance the statement is true is 1/3
    # 5) We can now solve: 'car != door' = 1 - 'car == door' =  1 - 1/3 = 2/3

    return random() < 2/3
    
def run(simulateFunc: callable, n: int, fixedSeeds: bool = False) -> float:
    wins: int = 0
    runs: int = 0
    while runs < n:
        if fixedSeeds: seed(runs) # When true, used to show simulate and simualteSimplified are functionally the same
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