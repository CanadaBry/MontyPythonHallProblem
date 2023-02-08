from random import randint, random, seed

def simulate() -> bool:
    available_doors: list = [1,2,3] # Represents the 3 doors

    car_door: int = randint(1,3) # Pick one door at random to have the car in it
    player_door: int = randint(1,3) # Player picks one door at random

    available_doors.remove(player_door) # Remove the player's door from the available doors

    # Host opens an available door
    if car_door in available_doors: # Host cannot open the door with car in it
        available_doors = [car_door] # So we remove the door without the car
    else: # Player's door is the car
        available_doors.pop(randint(0,1)) # We can remove either door
    
    switch_door: int = available_doors[0] # Assign the door the player has the option to switch with

    won: bool = switch_door == car_door # Check if the player wins if they switch

    return won

def simulateSimplified() -> bool:
    # Pick Car Door and Player's Door
    car_door: int = randint(1,3)
    player_door: int = randint(1,3)

    # Below is the simplified logic from the above function:
    # 1) The statements 'available_doors.remove(player_door)' and 'if car_door in available_doors' can be simplified to 'if car_door != player_door'
    # 2) Implicitly, the player wins if they switch to the car door, so the body of the 'if' can simpified to 'won = True'. This can then be further simplified to 'return True'
    # 3) Similarily, the player cannot win by switching if they picked the door with the car, so the 'else' can be simplified to 'return False'
    #
    # The pattern is now: 
    #
    # if car_door != player_door: 
    #   return True
    # else: 
    #   return False 
    #
    # This can be simplified to 'return car_door != player_door'

    return car_door != player_door 

def simulateSimplifiedFurther() -> bool:
    # Let's solve for the probability of 'car_door != player_door'
    # 1) Inverting the probability: Chance of 'car_door != player_door' = 1 - Chance of 'car_door == player_door'
    # 2) Replace the variables, with their values: 'car_door == player_door' -> 'randint(1,3) == randint(1,3)'
    # 3) Break the problem into cases based on value chosen in first randint(1,3): 'randint(1,3) == randint(1,3)' -> '1 == randint(1,3)', '2 == randint(1,3)', '3 == randint(1,3)'
    # 4) We can observe no matter what is chosen for the first randint(1,3), the chance the statement is True is 1/3
    # 5) We can now solve: 'car_door != player_door' = 1 - 'car_door == player_door' =  1 - 1/3 = 2/3

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