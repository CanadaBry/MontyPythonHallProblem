# Monty (Python) Hall Problem
 Using programming and python to explain the Monty Hall Problem.

 Pre-requsite Knowledge:
 - Understanding of if/else statements, arrays and boolean expressions
 - Know how randint() and random() from Python's Random library work
 - Python programming language syntax
 - General understanding of probability is a plus

The functions in this program are designed to return *True* if switching doors would result in the player winning the car.

## Simulation Functions:

**simulate**: Written to be as true to the Monty Hall Problem as possible. Not programically optimized.

**simulateSimplified**: Takes the *simulate* function and iterates by simplifying the core logic. This simplification is designed to explain the Monty Hall Problem.

**simulateSimplifiedFurther**: Iterates further on *simulateSimplified*, reducing all logic down to a basic probability of success.

## Helper Functions:

**run**: Used to run many iterations on our simulation functions and return the win rate.

## Executation

We run *simulate* and *simulateSimplified* with the same sample size and same seeds. 
- The results show the "simulated" probability of success if a player switches their door in the Monty Hall Problem. 
- We use fixed seeds so *simulate* and *simulateSimplified* return the same results, proving they are functionally the same.