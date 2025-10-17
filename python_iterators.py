# # iterators
# num = [1, 2, 3]

# for i in num:
#     print(i)


# L = [x for x in range(1, 100)]

# # for i in L:
# #     print(i * 2)

# import sys

# print(sys.getsizeof(L)/1024)

# X = range(1, 10000000)
# # for i in X:
# #     print(i * 2)

# print(sys.getsizeof(X)/1024)


# T = (1, 2, 3)
# dir(T)
# print(dir(T))

# dic = {"key": "value", "almo": "dush" }
# print(dir(dic))

# def itet(iterable):
#     iterable = iter(iterable)

#     while True:
#         try:
#             print(next(iterable))
#         except StopIteration:
#             break

# a = (1, 2, 3, 4)
# b = [1, 3, 5]
# c = range(1, 11)
# d = {"A": 2, "V": 3}

# itet(a)

# num = [1, 2, 3]
# iter_obj = iter(num)

# print(id(iter_obj), "Adress of itertor 1")


# r1 = iter(iter_obj)
# print(id(r1), "Adress of the itertro 2")



# class mera_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return mera_range_iter(self)

# class mera_range_iter:
#     def __init__(self,itertor_obj):
#         self.iterable = itertor_obj

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.iterable.start >= self.iterable.end:
#             raise StopIteration
        
#         current = self.iterable.start
#         self.iterable.start += 1

#         return current
    
# x = mera_range(1, 11)
# print(iter(x))


#Generator of python

# def gen_demo():
    
#     yield "Frist Statement"
#     yield "Second Statement"
#     yield "third Statement"

# gen = gen_demo()

# for i in gen:
#     print(i)


# def squre(num):

#     for i in range(1, num + 1):
#         yield i*2

# gen = squre(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for d in gen:
#     print(d)


def mere_range(start, end):

    for i in range(start, end):
        yield i


for d in mere_range(15, 26):
    print(d)

        

        
