##Used then for mapping. A dictionary maps a set of objects (keys) to another set of objects (values).

#Use {} curly brackets to construct the dictionary, and [] square brackets to index it
#Separate the key and value with colons : and with commas , between each pair.

#A Python dictionary is a mapping of unique keys to values
#Dictionaries are mutable, which means they can be changed.
#The values that the keys point to can be any Python value. Dictionaries are unordered, so the order
#that the keys are added doesn't necessarily reflect what order they may be reported back.

#Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like
#['key'] is not allowed. *key specified as key is not allowed
#Values pointed from keys can change and be pointing to alists

#Methods: clear, del, comp, len, type

#Dictionaries are unordered in Python. If you do not care about the order of the entries and want to access the
#keys or values by index anyway, d.keys()[i]. If you do care about the order of the entries use a list of pairs
#l = [("blue", "5"), ("red", "6"), ("yellow", "8")]

#No issue if defined twice, duplicate keys are removed. Last assignment wins
released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2008,
		"iphone 4" : 2010,
		"iphone 4" : 2011,
	}
print (released)

#Access by key value
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])

#Updated a key
dict['Age'] = 8

#Save a key value as list
dict['Age'] = [8]

#Added a new key with value
dict['School'] = "DPS School"; # Add new entry

print ("dict: ", dict)
print ("dict['Age']: ", dict['Age'])

#Methods
del dict['Name']; # remove entry with key 'Name'
print ("dict: ", dict)
dict.clear();     # remove all entries in dict
print ("dict: ", dict)
del dict ;        # delete entire dictionary

#Keys specified as list not allowed
NameKey = ("Name")
#NameKey = ["Name"]
dict = {NameKey: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict['Name'])

#Change a Key specified as set
NameKey = ("FirstName")
dict = {NameKey: 'Zara', 'Age': 7}
print ("dict['FirstName']: ", dict['FirstName'])

#methods
print ("dict keys: ", dict.keys())
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("Value : %s" %dict)