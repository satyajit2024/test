l = [1,2,3,4,3,2,4,5,2,7]
print(min(l))
def hello(ps):
    return (*ps,)

h = hello(l)
print(h)


# lis = {}

# for i in l:
#     if i in lis:
#         lis[i] += 1
#     else:
#         lis[i] = 1

# copy_lis = lis.copy()
# for key in copy_lis:
#     if lis[key] < 2:
#         del(lis[key])

# # print(copy_lis)
# print(lis)
# # print(lis)
# # lis[1]=10
# # print(lis)