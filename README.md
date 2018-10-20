# stackulator

this is for the implementation of a simple RPN shell

this will take in an RPN expression from the user delimited by spaces.
then the text is broken up into 2 stacks, 1 for data, and 1 for functions
then the stacks are evaluated

example:

input expression

2 3 + 5 *

stack diagram

func: + *
data: 2 3 5

