num_list = []
for i in range(10000):
  num = i
  sum = num
  while(num>0):
    sum += num % 10
    num = num // 10
  num_list.append(sum)  

for i in range(10000):
  if (i not in set(num_list)):
    print(i)