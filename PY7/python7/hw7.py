


# დავალება 1.

# შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს
# რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.




# int_list = [10, 20, 30, 40]

# def insert_element(element):
#    global int_list
#    int_list.append(element)  
#    return int_list

# element = 50
# result = insert_element(int_list)
# print(result)

# დავალება 2.

# შექმენით ფუნქცია, რომელიც ატრიბუტად იღებს წინადადებას, ფუნქციამ უნდა დააბრუნოს წინადადებაში არსებული სიტყვებიდან ყველაზე დიდი.
# მინიშნება: შეგიძლიათ გამოიყენოთ სტრინგის მეთოდი split()



# def str_sentence (string):
#     words = string.split()
#     max_word = max(words, key=len)
#     return max_word

# დავალება 3.

# დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
# პარამეტრად უნდა მიიღოს შემდეგი სია [100,20,30,50,5323,3321,22,56,700,90,10]

# list =[100,20,30,50,5323,3321,22,56,700,90,10]

# def sum_numbers (list):
#     total_sum=list.Math.fsum(list) 
#     return total_sum

# დავალება 4.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად იღებს ლისტს, ფუნქციამ უნდა დააბრუნოს ახალი ლისტი,
# რომელშიც მოცემული იქნება მხოლოდ ის მნიშვნელობები, რომელიც უნიკალურია(მხოლოდ ერთხელაა გამოყენებული) ატრიბუტად გადმოცემულ ლისტში.

# list=[10,11,20,10,20,15,16,16]

# def filter_list (list):
#     unique_list = list(set(list))
#     return unique_list

# დავალება 5.

# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და
# დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან
# 1+2+3+4+5 უდრის 15-ს )


# def sum_numbers (number):
  
#     if number < 10:
#         return number
    
#     last_number = number % 10
#     remaining_number = sum_numbers(number // 10)  

#     return last_number + remaining_number


# number = 12345
# result = sum_numbers(number)
# print(f"The sum {number} is: {result}")

# დავალება 6.

# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და
# დააბრუნებს მის შებრუნებულ (revers) სტრიქონს ( მაგალითად input:Hello Output: olleH)



# def reverse_string(string):
#     return string[::-1]

# input_string = "Hello"

# result = reverse_string(input_string)

# print(f"Reversed string: {result}")


# დავალება 7.

# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს და დაგვიბრუნებს ფაქტორიალს ამ რიცხვის ჩათვლით.

# import math

# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * math.factorial(number-1)
    
# number = 3
# result = factorial(number)
# print(f"factorial of {number} is: {result}")