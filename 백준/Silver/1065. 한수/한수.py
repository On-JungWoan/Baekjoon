N = int(input())

cnt = 0
for i in range(1, N+1):
  dif = []
  while(i>0):
    res = i % 10
    i //= 10
    if(i>0):
      dif.append(res - i%10)

  if (len(dif)<2): cnt += 1
  else:
    k = 0
    for j in range(len(dif)-1):
      if(dif[j] == dif[j+1]): k += 1
    if(k == len(dif)-1): cnt += 1
print(cnt)