t = input().split()
N = int(t[0]); r = int(t[1]); c = int(t[2])

res = 0
while(True):
  # break문
  if N==0:
    res += (int(r//0.5) + c)
    break  

  # 큰 덩어리 좌표
  loc_r = r // 2**N
  loc_c = c // 2**N

  # 큰 덩어리 기준 세부 좌표
  r = r % 2**N
  c = c % 2**N

  # 좌표 계산
  res += (int(loc_r//0.5) + loc_c) * 4**N
  N -= 1

print(res)