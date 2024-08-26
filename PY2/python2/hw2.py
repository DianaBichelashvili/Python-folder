

# # 1 დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი ‘even’ თუ კენტია ‘odd’

number= int(input("Enter a number:"))

 if number % 2 == 0:
       print("{number} is even")
 elif number% 2 !=0:
      print("{number} is even")

 else: 
    print("enter a number")     


def EvenNumber (number):
    if number%2!=0:
        print("{number} is not even")

    elif number==2:
       return number
    else:
        return EvenNumber(number-2)

EvenNumber (10)

# დავალება 2.

# დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნის სიტყვებს “small”, “tall”, “middle”
# 	a. თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაბეჭდეთ სიტყვა
	
# 	b. თუ ტექსტში არცერთი სიტყვა მოიძებნა დაბეჭდეთ, რომ ტექსტში ეს 	სამი სიტყვა არ მოიძებნა


# str_text = input("Enter a text:")

# find_words = ['small', 'tall', 'middle']

# result= print("Find words are:"find_words) if find_words in str_text else print ("No words found")   


# და ესე თუ შეიძლება

# str_text = input("Enter a text:")

# find_word1 = 'small', 
# find_word2 = 'tall', 
# find_word3= 'middle'

# result= print("Find words are:", find_word1, find_word2, find_word3) if find_word1 in str_text or find_word2 in str_text or find_word3 in str_text else print ("No words found")
# ან

# if find_word1 in str_text
#     print("Find word1 is:", find_word1)
# elif find_word2 in str_text
#     print("Find word2 is:", find_word2)
# elif find_word3 in str_text
#     print("Find word3 is:", find_word3)

# else: print("No words found words")


# დავალება 3.

# დაწერეთ კალკულატორი, რომელიც შეგვეკითხება პირველ რიცხვს, შემდეგ მეორე რიცხვს, შემდეგ მათემატიკურ ოპერატორს და 
# შესაბამისი მათემატიკური ოპერატორის გამოყენებით დაგვიბეჭდავს შედეგს.


# number1 =int(input("enter the first number:"))
# number2 =int(input("enter the second number:"))
# operator = input("enter the operator (+,-,*,/):")

# if operator == '+':
#    result=number1+number2
#    print("The result is:", result)
# elif operator == '-':
#    result=number1-number2
#    print("The result is:", result)
# elif operator == '*':
#     result=number1*number2
#     print("The result is:", result)
# elif operator== "/":
#     result=number1/number2
#     print("The result is:", result)
# else: ("the input is not a number")    

