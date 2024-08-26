# დავალება 1.

# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount, ისეთი ატრიბუტებით,
# როგორიცაა account_number, account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები.
# შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.


# class BankAccount:

#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

     
#     def payment(self, amount):
#         if amount > self.balance:
#             print("Balance is not enough!")
#         else:
#             self.balance -= amount
#             print(f"Payment {amount} made. Remaining balance: {self.balance}")
   
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposit {amount} made. New balance: {self.balance}")


# Client1 = BankAccount ("12345", "John Doe", 1000)
# Client1.payment(500)
# Client1.deposit(2000)


# Client2 = BankAccount ("678910", "Jane Doe", 2000)
# Client2.payment(4000)
# Client2.deposit(1000)





# დავალება 2.

# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, student_id და courses(კურსების სია,
#  რომელშიც სტუდენტი არის ჩარიცხული). აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები.
# შექმენით რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.



# class Student:

#     Javascript_Course_length=2 
#     Javascript_Course_price=1000
    
#     Python_Course_length=2 
#     Python_Course_price=2000



#     def __init__(self, name, student_id, courses):
#         self.name = name
#         self.student_id = student_id
#         self.courses = courses


#     def add_course(self, course):
#         self.courses.append(course)
#         print(f"{course} added to {self.name}'s courses")



# student1= Student("Anna", 12345)
# student1.add_course("Python")
# student1.Python_Course_length
# student1.Python_Course_price
 
# student2= Student("John", 678910)
# student2.add_course("JavaScript")
# student2.Javascript_Course_length
# student2.Javascript_Course_price


