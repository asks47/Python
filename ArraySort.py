import array as arr
a = arr.array('d', [1.5, 1.4, 2.5, 1.1, 1.0]) 
for x in range(0,len(a)-1):
    for y in range(x+1,len(a)):
       if a[x] > a[y]:
          #print(a[x])
          temp = a[x]
          a[x] = a[y]
          a[y] = temp
for x in range(0,len(a)):
  print(a[x])
