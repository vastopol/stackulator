# stackulator

 a simple RPN shell with syntax flavored like forth
this takes in an expression from the user delimited by spaces.

## Example:

input

2 3 + 5 * .

output

25

## Special Commands:

exit  = quit program
.     = print stack
clear = empty stack
drop  = pop stack top
dup   = duplicate stack top
swap  = switch top 2 stack entries

## todo

build out the calculation part not using eval(string)
include the basic stack manipulation operators
work on implementing a 2 stack system
vector operations ie: [1,2] + [3,4] = [4,6]


see also:
http://wiki.laptop.org/go/Forth_stack_operators
http://astro.pas.rochester.edu/Forth/forth-words.html
http://galileo.phys.virginia.edu/classes/551.jvn.fall01/primer.htm
https://www.math.ubc.ca/~cass/vc/rpn/ca.html

