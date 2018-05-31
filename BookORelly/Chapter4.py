###Strings
#Polimorfism - El significado de una operación depende de los objetos con los
#objetos con los que opera, signo + en numeros suma en strings agrega
S = 'Spam'
print (len(S))
print(S[1:3])
print(S[0])
print(S[-2])
print(S[1:])
print(S[:3])
print('2 ' + S[:-1])
print("1 "+S[:])
S= 'z' + S[1:]
print(S)
S= 'shrubbery'
L = list(S) # Expand to a list: [...]
print(L)
L[1] = 'c' # Change it in place
print(L)
print('_'.join(L))
print(L)
B = bytearray(b'spam') # A bytes/list hybrid (ahead)
print(B)
print(B.extend(b'eggs'))
print(bytearray(b'spameggs'))
print(B.decode())
S= 'Spam'
print(S.find('pa'))
S.replace('pa', 'XYZ')
print(S.replace('pa', 'XYZ'))
print(S)
line = 'aaa,bbb,ccccc,dd'
print(line)
print(line.split(','))
print(S.upper())
print(S.isalpha())
line = 'aaa,bbb,ccccc,dd\n'
print(line)
print(line.rstrip())
print(line.rstrip().split(','))
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))
print('{:,.2f}'.format(296999.2567))
S = 'A\nB\tC'
print(len(S))
import re
print(re.split('[/:]', '/usr/home/lumberjack'))
L = [123, 'spam', 1.23]
print(len(L))
print(L[:-1])
print(L.pop(2))
print(L)
M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#comprehensions
row2 = [row[0] + 1 for row in M]
col2 = [column[1] + 1 for column in M]
print('###')
print(col2)
print(row2)
print(M)
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c * 2 for c in 'spam']
print(doubles)
a=list(range(1, 10, 2))
print(a)
b=[[x ** 2, x ** 3] for x in range(4)]
print(b)
print(b[0])
G = (sum(row) for row in M)
next(G)
a=next(G)
print(a)
#Dictionaries
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food'])
D['quantity'] += 1
print(D)
D = {}
D['name'] = 'Bob'
D['age'] = 40
print(D['name'])
name='Bob'
job='dev'
age=40
print("#####")
list1 = 'name', 'job', 'age'
list2 = 'Bob', 'dev', 40
bob2 = dict(zip(list1, list2))
print(bob2)
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],
'age': 40.5}
rec['jobs'].append('janitor')
print(rec)
print(rec['name']['last'])
print(rec['jobs'][-1])
D = {'a': 1, 'b': 2, 'c': 3}
D['e'] = 99
'f' in D
if not 'f' in D:
    print('missing')
value = D.get('x', 0)
print(value)
value2 = D['x'] if 'x' in D else 0
print(value2)
D = {'b': 1, 'a': 2, 'c': 3}
print(D)
Ks = list(D.keys())
print(Ks)
Ks.sort()
for key in Ks:
    print(key, '=>', D[key])
for C in 'spam':
    print(C.upper())
x = 4
while x > 0:
    print('spam!' * x)
    x -=1
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x**2)
print(squares)
#Tuples
T = (1,2,3,4)
T = T + (5, 6)
print(T)
T = (2,333,) + T[1:]
print(T)
T = 'spam', 3.0, [11, 22, 33]
print(T[2][1])
#files
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()
f = open('data.txt')
text = f.read()
print(text.split())
#decoding-encoding unicode
S= 'sp\xc4m'
print(S[2])
file = open('unidata.txt', 'w', encoding='utf-8')
file.write(S)
file.close()
raw = open('unidata.txt', 'rb').read()
print(raw)
print(len(raw))
text.encode('utf-8')
print(raw.decode('utf-8'))
#sets-unordered and inmutable lists
X = set('spams')
Y = {'h', 'a', 'm'}
print(X)
print(set('spam') == set('asmp'))
L = [None] * 100
print(type(L))
if type(L) == type([]):
    print('yes')

    class Worker:
        def __init__(self, name, pay):  # Initialize when created
            self.name = name  # self is the new object
            self.pay = pay

        def lastName(self):
            return self.name.split()[-1]  # Split string on blanks

        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)  # Update pay in place

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.lastName())
print(sue.lastName())
bob.giveRaise(.10)
sue.giveRaise(.10)
print(sue.pay)
print(bob.pay)
print("Chapter4")
