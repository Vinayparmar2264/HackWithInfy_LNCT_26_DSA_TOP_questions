# d = [2,4,6]
# value = [5,7,9]
# m = 5

# size = int(input().rstrip())
# m = int(input().rstrip())
# value = []
# d = []
# for i in range(size):
#     v = int(input())
#     value.append(v)
# for i in range(size):
#     v = int(input())
#     d.append(v)
# print(value,d)



# def foodStamp(value,d,m):
    # value1 = value.copy()
    # value1.sort()
    # max_point = 0
    # count = 0
    # for i in range(len(value1)-1,-1,-1):
    #     if count < m :
    #         max_point += value1[i]
    #         count+=1
    #     if count>=m:
    #         break


#     fraction = []
#     for i in range(len(value)):
#         temp = value[i]/d[i]
#         fraction.append((value[i],temp,1))
#     fraction.sort(key = lambda x : (-x[1]))
#     print(fraction)

#     j = 1
#     while count<m:
#         for i in range(len(fraction)):
            
#             if count < m :
#                 temp = fraction[i][0] - d[i]*(fraction[2] - 1)
#                 temp1 = fraction[i+1][0] - d[i+1]*(fraction[2] - 1)
#                 if temp > temp1:
#                     max_point += temp
#                     count+=1
                
#         j+=1
#     print(count)
#     print(max_point)




# def food_stamp(value,dec,meal):
#     val = value.copy()
#     val.sort()

#     max_points = 0
#     for i in range(len(val)-1,-1,-1):
#         if meal>0 :
#             max_points += val[i]
#             meal-=1
#         if meal<=0:
#             break
#     print(meal)
#     value1 = []
#     for i in range(len(value)):
#         value1.append([value[i],dec[i],2])
    
#     value1.sort(key = lambda x : (x[0]/x[1]),reverse = True)
    

#     i = 0
    
#     while meal > 0 and i < len(value1)-1:
#         temp = value1[i][0] - value1[i][1]*(value1[i][2]-1)
#         temp1 = value1[i+1][0] - value1[i+1][1]*(value1[i+1][2]-1)
#         if temp > temp1:
#             value1[i][2]+=1
#             meal -= 1
#             max_points += temp
#         else:
#             i+=1
#             value1[i][2] += 1
#             meal -= 1
#             max_points += temp1

#     return max_points




import heapq



def max_taste(N,M,v,d):
    # we will implement the max heap using negative sign with value
    heap  = []
    
    for i in range(N):
        heapq.heappush(heap,(-v[i],i))
    total_taste = 0
    
    for _ in range(N):
        if not heap:
            break

        value,i = heapq.heappop(heap)
        value = -value

        if value <= 0:
            break

        total_taste += value

        next_value = value - d[i]

        if next_value > 0:
            heapq.heappush(heap, (-next_value,i))
    return total_taste

if __name__ == "__main__" :
    size = int(input())
    m = int(input())
    value = []
    dec = []
    for i in range(size):
        v = int(input())
        value.append(v)
    for i in range(size):
        v = int(input())
        dec.append(v)
    print(max_taste(size,m,value,dec))

    # time complexity is O(M log N)
