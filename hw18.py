
დავალება 1.

დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს, დაუწერეთ დეკორატორი, რომელიც შეამოწმებს,
 რომ რიცხვი უნდა იყოს დადებითი, თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით, 
 სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან.


def return_number(n):
    return n
def check_positive(func):
def wrapper(n):
        if n < 0:
            raise ValueError("The number must be positive.")
        return func(n)
    return wrapper

    @check_positive
def return_number(n):
    return n