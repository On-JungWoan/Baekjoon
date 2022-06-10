N = int(input())
vote_list = []
for i in range(N):
  vote_list.append( int(input()) )

dasom = vote_list[0]
candi = vote_list[1:]

if(N == 1):
  print(0)

else:
  num = 0
  candi = sorted(candi, reverse=True)
  while(candi[0] >= dasom):
    dasom += 1
    candi[0] -= 1
    num += 1
    candi = sorted(candi, reverse=True)

  print(num)