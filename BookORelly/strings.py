#inmutable
#S1 = 'splot'
#S1[0] = "x"
#print(S1)
#Contain text
#support slicing and methods
#update" an existing string by (re)assigning a variable to another string.

text = 'The surface of the circle is 2 pi R = '
text1 = "The surface of the circle is 2 pi R = "
text2 = '''The surface of the circle is 2 pi R = '''

print(text[0])
print(text1[-2])
print(text2[0:])

#text[0] = 'a' #this is incorrect.

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
print("XXXXXXXX1")

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
print(type(S))
print("XXXXXXXX2")

line = 'aaa,bbb,ccccc,dd\n'
print(line)
print(line.rstrip())
print(line.rstrip().split(','))
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))
print('{:,.2f}'.format(296999.2567))
S = 'A\nB\tC'
print(len(S))
print("XXXXXXXX3")

#extended slice
S = 'abcdefghijklmnop'
print(S[::2])
print(S[1:10:2])
num = 1 / 3.0
print(num)
print('%4.2f' %num)

S = 'abcdefghijklmnop'
print(S[1:10:2])
S = 'hello'
print(S[::-1])

#String methods

S = 'splot'
print(S.replace('pl', 'pamal'))
print('That is %d %s bird!' % (1, 'dead'))
S = 'spam'
print(S.find('pa'))
S = 'spammy'

print(S[:3] + 'xx' + S[5:])
print(S.replace('mm', 'xx'))

str = "this is string example....wow!!!"
sub = "t"
print ("str.count(sub, 4, 40) : ", str.count(sub, 0, 1))
sub = "example"
print ("str.count(sub) : ", str.count(sub))

#strings with sets to dictionaries?
template = '{motto}, {pork} and {food}' # By keyword
L= template.format(motto='spam', pork='ham', food='eggs')
print(L)
