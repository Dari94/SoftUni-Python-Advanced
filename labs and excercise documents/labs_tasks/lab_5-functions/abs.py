def to_abs_list(values):
   # return [abs(x) for x in values]
   return list(map(abs,values))

print(to_abs_list(map(float,input().split(' '))))
