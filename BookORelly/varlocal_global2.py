import var_global
from varlocal_global import globalfunc


print("Imported function:")
globalfunc()

var_global.init()

def stuff():
    var_global.myList.append('global2')
    print("Global var from settings:", var_global.myList)
    print("Global var from settings:", var_global.wxk)
    x = 1
    print("X in stuff:",x)
    var_global.wxk += var_global.wxk

stuff()
#Shared outside of the function
var_global.myList.append('hey2')
print("Global var from settings:", var_global.myList)