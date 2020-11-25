def myMap(function, iterable):
    result = []
    for i in iterable:
        result.append(function(i))
    return result
    


def myfunc(a):
  return len(a)

x = myMap(myfunc, ('apple', 'banana', 'cherry'))

print(x)