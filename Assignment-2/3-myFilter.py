def myFilter(function, iterable):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    return result


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = myFilter(myFunc, ages)

for x in adults:
  print(x)