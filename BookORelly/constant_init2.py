#Note: In reality, we don't use constants in Python. The globals
# or constants module is used throughout the Python programs.

import constant_init

print(constant_init.PI)
print(constant_init.GRAVITY)

#Overwritting
PI = 3.18
print(PI)