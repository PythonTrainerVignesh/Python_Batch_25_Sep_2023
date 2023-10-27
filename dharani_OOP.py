# Today class about the object orient programing.
# "Class" is a collection of object blueprint.
# It has "Methods" in class work


# from Object_orient import (add, subtract)
#
# print(add(5, 8))
# print(subtract(15, 29))
#
# import Object_orient
#
# print(Object_orient.add(5, 17))
# print(Object_orient.subtract(5, 17))

from Object_orient import ReportCard
from Object_orient import BankAccount
from Object_orient import Products

# Instance is a copy of class.

class_10 = ReportCard()
class_9 = ReportCard()
class_8 = ReportCard()
# Bank account problem

account1 = BankAccount(0, "B", "Dharani", "23DP45FF", 2342343423, 234545433)

# account1.credit()

category_1 = Products("Mobiles", 15000, 5)
category_2 = Products("Laptops", 45000, 3)
category_3 = Products("Headphones", 500, 30)

print(category_1.total_price())
print(Products.all)

