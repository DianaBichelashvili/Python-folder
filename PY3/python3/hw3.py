
# დავალება1.
# დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდენ იყენებს while ციკლს, 
#     რომ რევერსულად დაბეჭდოს რიცხვები 0-მდე, მაგალითად თუ შეიყვანს რიცხვს 4, დაიბეჭდოს 4,3,2,1



# number= int(input("Enter a  number:"))


# while number >= 0:
#     print(number, end=" ")
#     number -= 1

# დავალება2.
# დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0,
# შეამოწმეთ რიცხვი, თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს, ეს პროცესი გაგრძელდეს მანამ, 
# სანამ მომხმარებელი არ შეიყვანს ტექსტს sum, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.


# total_sum = 0

# while True:
#     number = input("enter a number or word sum: ")
    
#     if number == 'sum':
#         break
    
#     if number>0:
#             total_sum += number

# print(f"Total Sum is: {total_sum}")


# დავალება3(არასავალდებულო).  
# დაწერეთ პითონის პროგრამა, რომელიც შემთხვევითობის პრინციპით აირჩევს რიცხვს ნებისმიერ შუალედში, ასევე აირჩიეთ სიცოცხლეების რაოდენობა, 
# რომელსაც შეინახავთ ცვლადში, პროგრამამ კი მომხმარებელს უნდა მოთხოვოს რიცხვის შეყვანა მანამ, სანამ არ წააგებს ან სანამ არ მოიგებს,
# თუ რიცხვს შევიყვანთ უფრო მაღალს, დაგვიბეჭდოს რომ რიცხვი მაღალია, თუ შევიყვანთ დაბალს დაგვიბეჭდოს რომ რიცხვი დაბალია.
# წაგების ან მოგების შემთხვევაში პროგრამა უნდა გაჩერდეს.

# გამოიყენეთ else ბლოკი while ციკლთან ერთად

# from random import randint

# random_number = randint (10, 50)
# life=5 

# while life>0
#   user_number=int(input("Enter a random number"))
#   if user_number>=random_number:
#    print ("Number is greater than  Random Number")
#    life -=1
#   elif user_number<random_number:
#     print ("Number is less than Random Number")
#     life -=1
#   elif  user_number==random_number:
#     print ("Congratulations! You guessed the number")
#     break
#   elif life==0:
#      print ( "You Lost Try Again")
#   else:
#      print ("Life Remaining:",life)