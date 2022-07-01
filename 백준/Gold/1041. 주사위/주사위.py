import sys

N = int(input())
dice = list( map(int, sys.stdin.readline().split()) )
min_list = sorted([min(dice[0],dice[5]), min(dice[1],dice[4]), min(dice[2],dice[3])])

if(N==1):
  print(sum(sorted(dice)[:5]))
else:
    print(sum(min_list[:2])*4*(1+(N-2)*2) + sum(min_list)*4 + min_list[0]*(N-2)*(4+(N-2)*4+(N-2)))