class MyClass:
  def __init__ (self,mydict):
    self.mydict = mydict
  def multipl_key (self, key):
    a = self.mydict.get(key,0)
    if a==0:
      print("Key not found:",key, "; Product of multiples of three = 0")
    else:
      b = 1
      for i in a:
        if i%3 == 0:
          b = b*i
      if b != 1:
        print("Key = ", key, "; Product of multiples of three (0 is a multiple of three) =", b)
      else:
        print("Key = ", key, "; There are no multiples of three")
e1 = MyClass({'a': [1,2,7,4,5],'b': [],'c': [1,2,3,4,5,-6]})
print("DICTIONARY1 {'a': [1,2,7,4,5],'b': [],'c': [1,2,3,4,5]}")
e1.multipl_key('d')
e1.multipl_key('a')
e1.multipl_key('b')
e1.multipl_key('c')
e2 = MyClass({'a': [3,-3,9,-27,5],'b': [1,2,1,1,2],'c': [-3,-3,0,27,33]})
print("DICTIONARY2 {'a': [3,-3,9,27,5],'b': [1,2,1,1,2],'c': [-3,-3,0,27,33]}")
e2.multipl_key('Privet')
e2.multipl_key('a')
e2.multipl_key('b')
e2.multipl_key('c')
e3 = MyClass({'a': [-3],'b': [3],'c': [1]})
print("DICTIONARY3 {'a': [-3],'b': [3],'c': [1]}")
e3.multipl_key('Hi')
e3.multipl_key('a')
e3.multipl_key('b')
e3.multipl_key('c')