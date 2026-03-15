ranked = [100,100,50,40,40,20,10]
player = [5,25,50,120]

ranked = sorted(set(ranked))
r = len(ranked)
result =[]
i = 0
for score in player:
  while(i<r and ranked[i]<=socre):
    i+=1
  result.append(r-i+1)
return result
