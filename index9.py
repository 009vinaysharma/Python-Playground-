 # def add(n,):
 #     if n==1:
 #         return 1
 #     return n +add(n-1)

# print(add(10))





# def factorial(n):
#     if n==0 or n==1:
#          return 1
#      else:
#          return n * factorial(n-1)
#         print(n)

#  print(factorial(20))



#  def fabonacci(n):
#      if n<=0:
#          print("Incorrect input")
#      elif n==1:
#          return 0
#      elif n==2:
#          return 1
    
#       return fabonacci(n-1)+fabonacci(n-2)
#  for i in range(1,11):
#       print(fabonacci(i))





#  add=lambda a,b : a+b
#  print(add("tanish"+" "," khan"))





# def abc(function):
#     def wrapper():
#         function()
#     return wrapper()

# @abc
# def xyz():
#     print("xyz")



# xyz()

# import time
# print(time.time())





# def timemeasure(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result
#     return wrapper
# @timemeasure
# def pause():
#     time.sleep(5)
#     print("Function paused for 5 seconds")
# @timemeasure
# def quick():
#     print("Quick function executed")

# timemeasure(20)


import time
def timemeasure(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        n=print(end - start)
        return n
    return wrapper
@timemeasure
def add(n):
     if n==1:
         return 1
     else:
         return n() + add(n-1)

# @timemeasure
# def quick():
#     print("Quick function executed")


print(add(10))
