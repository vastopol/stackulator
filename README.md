# stackulator

this is for the implementation of a simple RPN shell (not done yet...)

the idea is to take in a line of text form the user delimited by spaces.
then the text is broken up into 2 stacks, 1 for data, 1 for functions
when the user enters a symbol then the stacks begin executing

special notations:
. = show stacks
! = run stacks
@ = load txt file

input:
2 3 + 5 *

stacks:
2    +
3    *
5
