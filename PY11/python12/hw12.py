დავალება 1.

შექმენით ცვლადი squared_numbers რომელიც შეიცავს 1-დან 10-ის ჩათვლით კვადრატში აყვანილ რიცხვებს(არ შეავსოთ ხელით)

squared_numbers = [x**2 for x in range(1, 11)]


დავალება 2.

დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს სტრინგს, დააბრუნეთ სეტი, რომლის ელემენტებიც არის სტრინგში არსებული თითოეული სიმბოლო

def element_in (string):
    return set(string)

string1 = "hello world"
string2 = element_in (string1)

print(string2)

დავალება 3.

დაწერეთ ფუნქცია რომელიც ატრიბუტად მიიღებს ორ tuple ტიპის მონაცემს, ფუნქციამ უნდა გააერთიანოს ეს ორი tuple და დააბრუნოს ერთი მთლიანი დუბლიკატების გარეშე,
შექმენით სია duplicated_values და მასში დაამატეთ ის ინფორმაცია მხოლოდ ერთხელ, რომელიც დუბლირებული სახით გვხვდება tuple-ში, დაბეჭდეთ მოცემული სია


def func_combine_tuples (tuple1, tuple2):
    combined_tuple = tuple1 + tuple2
    duplicated_values = [x for x in combined_tuple if combined_tuple.count(x) > 1]
    return combined_tuple, duplicated_values


example:
tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

output:
combined_tuple: (1,2,3,4,5,6,7)
duplicated_values: [4,5,6]



დავალება 4.

დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს ტაპლს, დააბრუნეთ ტაპლი სადაც პირველ და ბოლო ელემენტს შეცვლილი ექნება ადგილები:

def swap_elements (tuple):
    return tuple[-1:] + tuple[1:-1] + tuple[:1]

input: (1, 2, 3, 4)
output: (4, 2, 3, 1)



დავალება 5.

დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს ერთმანეთში ჩადგმულ ტაპლს, დააბრუნეთ ერთი სრული ტაპლი, სადაც მოცემული იქნება ყველა ელემენტი.


def combine_tuple (nested_tuple):
    commbined_tuple = [item for list in nested_tuple for item in list]
    return combine_tuple(commbined_tuple)

Input: (1, (2, 3), (4, (5, 6)))
output: (1, 2, 3, 4, 5, 6)


დავალება 6.

დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს ორ სეტს, დააბრუნეთ სეტი, რომელიც შედგება ტაპლებისგან და ისინი შეიცავენ ორი სეტის ყველა შესატყვისს:

def combine_tuples (tuple1, tuple2):
    return tuple1 + tuple2


updated_tuple=tuple1.difference_update(tuple2)
print (updated_tuple)

tuple1={1, 2}

tuple2={‘a’, ‘b’}

input: {1, 2}{‘a’, ‘b’}
output: {(1, ‘a’), (1, ‘b’), (2, ‘a’), (2, ‘b’)}


 
def combine_tuples (tuple1, tuple2):   
    return tuple1 + tuple2

return {(x, y) for x in tuple1 for y in tuple 2}


 outputი რომ მივიღოთ ფორი უნდა იყოს უფრო მემგონი მაგრამ ზემოთ difference -იც ვცადე გამომეყენებინა მაგრამ მაგ შემთხვევაში თითო ელემენტი მხოლოდ ერთხელ აისახება ხომ?
 