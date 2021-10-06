# import os
# os.system('cls' if os.name =="nt" else 'clear')

# def printtype(data):
#     for i in data:
#         print(i, type(i))

# test = [123 , 'Hilmi' , [1,2,3], (1,2,3), True]

# # printtype(test)

# class Person():
#     name='Isim'
#     age= 0

# person1= Person()
# person2 = Person()

# # print(person1.name)

# Person.job = 'teacher'
# print(person1.job)
# print(person2.job)


# ------------------------------------------------
# # Class attributes ve instance attributes
# person1.name='Rafe'
# print(person1.name)
# print(person2.name)
# ------------------------------------------------
#SELF Keyword
# class Person :
#     name='Isim'
#     age=0
#     count = 0
#     def test(self):
#         print('test')
#     def get_details(self):
#         print('name:', self.name, 'age:', self.age, 'location:', self.location)
#     def set_details(self , name , age, location):
#         self.name = name 
#         self.age = age
#         self.location = location
#     def plus(self):
#         self.count += 1
    
#     @staticmethod
#     def salute():
#         print('Hi', Person.name)


# person1 = Person()
# person1.test()
# Person.test(person1)
# person1.get_details()
# Person.salute()
# person1 = Person()
# person1.set_details('Hilmi', 27, 'Paderborn')
# person1.salute()

# print(person1.plus())

# class Dortislem:
#     count = 0
#     def plus(self):
#         self.count += 1
#         print(self.count)

# islem1 = Dortislem()
# islem2 = Dortislem()

# islem1.plus()
# islem1.plus()

# islem2.plus()
# islem2.plus()

# ----------------------------------------------

# #Special Methods - Object üreten özel fonksiyon yani constructor, Dont Repeat Yourself (DRY)
# https://docs.python.org/3/reference/datamodel.html
# person1 = Person()
# person1.set_details(...) kullanarak person1 i sonradan güncellemek yerine
# person1 = Person(....) şeklinde yazıp person1 i oluştururken istediğimiz değerleri veriyoruz
# class Person:
#     company = 'Clarusway'
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#         self._id = 5000 # Paython js gibi yasakci bir dil degil, bunu degistirebilirsin
#         self.__id1 = 4000 # Ama illa degismesin istiyorsak basina iki cizgi
    
#     def __str__(self): # attribute lari göstermek icin
#         return f'Name: {self.name} , Age:{self.age}'
    
#     def __len__(self): 
#         return self.age

    

# hilmi = Person('Hilmi',27)
# print(hilmi.name, hilmi.age)

# lst = [1 , 2 , 3]
# print(lst)
# print(len(lst))
# print(hilmi)
# print(len(hilmi))
# print(hilmi._id)
# hilmi._id = 3000
# print(hilmi._id)

# print(hilmi.__id1) # icinde id1 olmasina ragmen erisim yetkisi vermiyor
# # hilmi._id = 3000
# # print(hilmi.__id)
# -----------------------------------------------------------------------------

#inheritance and polymorphism
# class Person:
#     company = 'Clarusway'
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
    
#     def __str__(self): # attribute lari göstermek icin
#         return f'Name: {self.name} , Age:{self.age}'
    
#     def details(self):
#         return f'Name {self.name} Age : {self.age}'

# class Lang:
#     def __init__(self,langs):
#         self.langs = langs

# class Employee(Person, Lang): # Kendim de bastan nit yazabilirdim oun yerine super kullandim
#     def __init__(self,name,age,path):
#         # self.name = name
#         # self.age = age
#         super().__init__(name,age)
#         Lang.__init__(self,['Python','JS'])
#         self.path = path
    
#     def __str__(self): # attribute lari göstermek icin
#         return f'Name: {self.name} , Age:{self.age}, Path:{self.path}'
    
#     #override
#     def details(self):
#         super().details()
#         print( f'Name {self.name} Age : {self.age}, Path:{self.path}' )
  

# emp1 = Employee('Hilmi', 27, 'FS')
# # print(emp1)
# print(emp1.details())
# print(Employee.mro()) #soyagacini gosterir

# #Djangoda  bu iki özellik(inheritance and polymorphism) cok kullanilacak, biz class yazmcaz ihtiyacimiz olan yerleri kullanicaz

# -------------------------------------
#inner class , yine  kullanacagiz

# from django.db import models
# class Article (models.Model):
#     first_name = models.CharField(max_length = 30)
#     last_name = models.CharField(max_length = 30)

#     class Meta:
#         ordering = ["last_name"]

# -------------------------------------------------

class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__id= 1234 #unique
        self.movements = [] 
    
    def __str__(self):
        return f'Name: {self.name}, age: {self.age} , Id: {self.__id}'
    
    def add_movement(self,amount, date, explain):
        self.movements.append({'amount' : amount, 'date': date, 'explain': explain})

    def all_movements(self):
        for i in self.movements:
            print(i['date'], i['amount'], i['explain'])
    
    def balance(self):
        return sum(i['amount'] for i in self.movements)
        # total=0
        # for i in self.movements:
        #     total += i['amount']
        # print(total)

custom = Customer('Hilmi', 27)
print(custom)
custom.add_movement(5000, '15.10.2021', 'Salary')
custom.add_movement(-1000, '16.10.2021', 'Rent')
custom.add_movement(-500, '17.10.2021', 'Bills')
custom.add_movement(-2000, '18.10.2021', 'Credit Card')
custom.all_movements()
print(custom.balance())

