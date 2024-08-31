
დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს, დაუწერეთ დეკორატორი, რომელიც შეამოწმებს,
 რომ რიცხვი უნდა იყოს დადებითი, თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით, 
 სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან.

def check_positive(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("The number is positive.")
        return func(number)
    return wrapper

@check_positive
def return_number(number):
    return number

def main():
    numbers = [20, -15, 10]
    for num in numbers:
        try:
            result = return_number(num)
            print(f"The result for {num} is {result}")
        except ValueError as error:
            print(error)




დაწერეთ დეკორატორი, რომელიც გამოთვლის ფუნქციის მოქმედების დროს და დაბეჭდავს ტერმინალში. დროის აღსაქმელად გამოიყენეთ time.time()


import time

def calculate_time (func):
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs) 
        start_time = time.time()  
        end_time = time.time()  
        function_time = end_time - start_time 
        print(f"Function '{calculate_time}' needs {function_time: } seconds to finish the function") 
        return result  
    return wrapper

შექმენით მეტაკლასი LoggingMeta, რომელიც ყოველი კლასის შექმნის დროს დაბეჭდავს თუ რა სახელის მქონე კლასი იქმნება.


class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class '{name}'")
        return super().__new__(cls, name, bases, attrs)
