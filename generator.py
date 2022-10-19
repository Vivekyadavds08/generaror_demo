# def disp(a,b):
#     yield a
#     yield b
# #x,y = disp(10,20)
# # print(x)
# # print(y)
# result =disp(10,20)
# # print(result)
# # print(type(result)
# # lst = list(result)
# # print(lst)
# # print(type(lst))
# print(next(result))
# print(next(result))
def show(a,b):
    while a<=b:

        yield a

        a+=1
result  = show(1,5)
print(next(result))
print(next(result))
for i in result:
    print(i)

