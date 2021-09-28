# solution 


num = int(input())
lst = list(map(int, input().split()))  # [1,  1, 2,  3, 4, 5, 5, 4]

mx = max([lst.count(i) for i in lst])

# mx = 0
# for i in lst:
#     count = lst.count(i)
#     if count > mx:
#         mx = count

print(mx)
