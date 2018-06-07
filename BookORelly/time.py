#Suspend execution for some seconds

import time

print("Start : %s" % time.ctime())
time.sleep(5)
print("End : %s" % time.ctime())

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)