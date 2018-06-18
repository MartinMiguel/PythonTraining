class result_args:

    def add(instanceOf, *args):
      if instanceOf == 'int':
         result = 0
      if instanceOf == 'str':
         result = ''
      if instanceOf == 'doub':
          result = 'My '
      for i in args:
          result = result + i
      return result

print(result_args.add('int', 3, 4, 5))
print(result_args.add('str', 'I', ' am', ' in', ' Python'))
print(result_args.add('doub','kiss'))
