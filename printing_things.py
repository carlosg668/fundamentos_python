"""
Developer : cristina lugo
creation date : 21-sept-2024
Description: Program to learn basic concepts.
Updates: TBD
"""
"""
# Examples with function of print().
print(" Welcome to course of Basic Knownlegde of \n Programming with Python \
      .......................................")

print("Only I am string ")
num_five = 5
print(num_five)
print (" Coverting this number to string " + str(num_five)) 

# Examples with function of input() and concatenation.
name = input('What is your name?\n')
conc1 = 'Hola ' + name
print(conc1)
conc2 = name + ' please continue to fill the form'
print(conc2)
"""
# Examples to review methods of strins
concatatenation_one = 'amigo'
concatatenation_one_upper = concatatenation_one.upper()
concatatenation_one_low = concatatenation_one.lower()
concatatenation_one_cap = concatatenation_one.capitalize()

import pdb
pdb.set_trace()

# Examples convert int to string then concatenation with a validation.
concatatenation_one = 'amigo'
concatatenationOne = 5.5

if type(concatatenationOne) is str:
    print("Direct concatenation")
    print(concatatenation_one + concatatenation_one)

elif type(concatatenationOne)is not str:
    print(" I will change data")
    conc3 = str(concatatenationOne)
    print("data was changed")
    print(concatatenation_one + conc3)