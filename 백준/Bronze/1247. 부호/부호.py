from sys import stdin

res=[]
for i in range(3):
  sum = 0
  for _ in range( int(stdin.readline()) ):
    sum += int(stdin.readline())
  res.append('-' if (sum<0) else '+' if (sum>0) else '0')
for i in res:
  print(i)