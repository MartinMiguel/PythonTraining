#https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/
#__get__(self, obj, type=None), returns value
#__set__(self, obj, value), returns None
#__delete__(self, obj), returns None

#Example 1
class MyDescriptor():
    """
    A simple demo descriptor
    """

    def __init__(self, initial_value=None, name='my_var'):
        self.var_name = name
        self.value = initial_value

    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value

    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        print("Hit...")
        self.value = value

class MyClass():
    desc = MyDescriptor(initial_value='Mike', name='descp')
    normal = 10

if __name__ == '__main__':
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)

# Example 2
from weakref import WeakKeyDictionary

class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance_obj, objtype):
        return self.age.get(instance_obj, self.req_age)

    def __set__(self, instance, new_age):
        if new_age < 21:
            msg = '{name1} is too young to legally imbibe'
            print(msg.format(name1=instance.name))
        else:
            #self.age[instance] = new_age
            print('{name_c} can legally drink in the USA {years_c} years'.format(name_c=instance.name, years_c=new_age))

    #def __delete__(self, instance):
       # del self.age[instance]


class Person:
    drinker_age = Drinker()

    def __init__(self, name2, age):
        self.name = name2
        self.drinker_age = age


p = Person('Miguel', 30)
p = Person('Niki', 13)
print(p.drinker_age)