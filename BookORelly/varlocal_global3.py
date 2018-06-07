import var_global
import varlocal_global
import varlocal_global2

#var_global.init()
#List value hold
print ("Varlocal_global3 settings:",var_global.myList)

#initialized again
var_global.init()
print ("Varlocal_global3 settings initialized:",var_global.myList)

#varlocal_global.stuff()