# def factorial(n):
#     if n <= 1:
#         return 1
#     return  n * factorial(n-1)

# print("5!={}, 3!={}, 11!={}".format(
#     factorial(5),
#     factorial(3),
#     factorial(11)
# ))

# def fibonacci(limit):
#     nums = []

#     current=0
#     next=1

#     while current < limit:
#         current, next = next, next+current
#         nums.append(current)

#     return nums


# for n in fibonacci(100):
#     print(n ,end=", ")

# print()
# printl("with yield")

# def fibonacci(limit):
#     current=0
#     next=1

#     while current < limit:
#         current, next = next, next+current
#         yield current

# test = fibonacci(100)
# for n in test:
#     print(n ,end=", ")


# lookup = {}

# lookup = dict()

# lookup = {'age': 42, 'loc': 'Italy'}
# lookup = dict(age=42, loc='Italy')

# print(lookup)
# print(lookup['loc'])


# lookup['cat'] = 'Fun code demos'

# if 'cat' in lookup:
#     print(lookup['cat'])


class Bill:

    def __init__(self, orderID, number):
        self.orderID = orderID
        self.number = number

    def __repr__(self):
        return "orderID : {} number : {}".format(self.orderID, self.number)
        
    @staticmethod
    def create_bill(orderID, number):
        return Bill(
            orderID,
            number
        )

    
testList = []
import random 

for i in range(0, 5):
    testList.append(Bill.create_bill(random.randint(1,100) , random.randint(1,100)))

testList.sort(key=lambda item: item.number)

print(testList)