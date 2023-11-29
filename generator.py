# GENERATORS

# LIST - all in one big chucnk, more mem, more time
# line by line -->> just a single digit per action, less mem!

def generator_func(num):
    for i in range(num):
        yield i*2

# for item in generator_func(1000):
  #  print(item)


g = generator_func(100)
# next() -> StopIteration if out of index
print(next(g)) # 0 -> 0*2=0
print(next(g)) # 1 -> 1*2 =2
print(next(g)) # 2 -> 2*2 =4
