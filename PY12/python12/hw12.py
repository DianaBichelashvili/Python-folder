# დავალება 1.

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს წინადადება, პროგრამას დააბეჭდინეთ დიქტის სახით
# რამდენჯერ არის თითოეული სიტყვა გამოყენებული წინადადებაში

# input: The wind howled and howled all night long
# output: {“the”: 1, “wind”:1, “howled”:2, “and”:1, “all”:1, ”night”:1, “long”:1}




# def count_words (string)
#     word_count = {}
#     words = string.lower().split()
    
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
            
#     return word_count
    
# user_input= string(input("The wind howled and howled all night long"))

# word_count = count_words(user_input)
# print("Output:", word_count)


# დავალება 2.

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ორი რიცხვი და ერთი მათემატიკური ოპერატორი,
#  ააწყვეთ კალკულატორი, რომელიც გამოთვლის შესაბამის მოქმედებას, გამოიყენეთ დიქტები, სადაც key მნიშვნელობებად იქნება მათემატიკური ოპერატორები



# number1 =int(input("enter the first number:"))
# number2 =int(input("enter the second number:"))
# operator = input("enter the operator (+,-,*,/):")

# operators={"operator":"+", "operator":"-", "operator":"/", "operator":"*"} 

# if operator in operators == "+":
#  result=number1+number2
#  print("The result is:", result)
#  elif operator in operators == "-":
#  result=number1-number2
#  print("The result is:", result)
#  elif operator in operators == "*":
#  result=number1*number2
#  print("The result is:", result)
#  elif operator in operators == "/":
#  result=number1/number2
#  print("The result is:", result)

#  else: ("the input is not a number")

 

# დავალება 3.

# comperhension-ის გამოყენებით დააგენერირეთ დიქტი, რომლის key მნიშვნელობები იქნება 1-დან 10-ის ჩათვლით რიცხვები, ხოლო value მათი კვადრატი


# squares = {x: x**2 for x in range(1, 11)}

# print(squares)

# დავალება 4.

# შექმენით დიქტი, რომელიც ინახავს ინფორმაციას დეპარტამენტების და თანამშრომლების შესახებ, 
# თითოეულ თანამშრომელს უნდა ჰქონდეს ატრიბუტები: სახელი, გვარი, ასაკი, ხელფასი. გამოთვალეთ საშუალო ხელფასი დეპარტამენტების მიხედვით.

# company_units= {
#     "Marketing": {
#         {"Name": "John","Lastname": "Smith", "Age": 30,"Salary": 5000}
#         {"Name": "Jane","Lastname": "Smith", "Age": 35,"Salary": 3000}
#     },
#     "Sales": {
#         {"Name": "Jack","Lastname": "Johnson", "Age": 30,"Salary": 6000}
#         {"Name": "Kate","Lastname": "Johnson", "Age": 25,"Salary": 6500}
#     }

#     "Finance": {
#         {"Name": "Tom","Lastname": "Johnson", "Age": 28,"Salary": 5500}
#         {"Name": "Anna","Lastname": "Johnson", "Age": 32,"Salary": 4500}
#     }
#     }

#    def average_salary (salary):
#     return sum(salary)/len(salary)
#     for department, employees in company_units.items():
#     print(f"Department: {department}", "salary: {salary}")




# დავალება 5.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს დიქტს, ფუნქციამ უნდა დააბრუნოს შებრუნებული დიქტი, 
# სადაც key მნიშვნელობები იქნება ორიგინალი დიქტის value და value იქნება ორიგინალი დიქტის key მნიშვნელობები


# def transform_dict (dictionary):
#     transformed_dict = {}
#     for key, value in dictionary.items():
#     return transformed_dict[key]
