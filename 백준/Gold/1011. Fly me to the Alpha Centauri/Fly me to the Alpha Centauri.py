import math
import sys

n = int(input())
data = []

for i in range(n):
  data.append(list(map(int, sys.stdin.readline().split())))

for d in data:
  # 두 수의 차이
  diff = d[1] - d[0]

  # 차이의 제곱근
  n = int(math.sqrt(diff))
  # 제곱근에 대해서 다음과 같은 등차수열이 성립함
  res = 2*n-1

  # 제곱근에서 n만큼 떨어진 수는 +1
  # 그렇지 않은 수는 +2
  if( diff - n**2 != 0 ):
    if( diff - n**2 > n ):
      res += 2
    else:
      res += 1

  print(res)