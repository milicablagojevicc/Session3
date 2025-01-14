#boolean are and, or, not
#Not: if x is false, then TRUE, else FALSE
#Or: if x is false, then y, else x
print(2 or 3) #is 2
print (2 or 3 or 4 or 5) #always 2 cuz you just need to look at 2
#And: if x is false, then x, else y
print(2 and 3) #is 3
print(2 and 3 and 4 and 5 and 0) #0 because it is the last value
#every link in the AND chain must be true
#All info in python is considered TRUE by default, EXCEPT: NONE, FALSE, 0, 0.0, EMPTY SEQUENCES...

#COMPARISON OPERATORS
# < less than
#<= less/eq
# > greater than
# >= greater/equal
# == equal to
# != not equal
# is - object identify - being the same thing
# is not - negated object identify


a = 5
print (a)
a += 2
print (a)
a -= 10
print(a)
a *= -2
print(a)
a %= 4
print(a)