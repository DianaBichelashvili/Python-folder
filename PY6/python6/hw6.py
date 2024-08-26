# დავალება 1.
# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრინგს და შეამოწმებს არის თუ არა სტრიქონი ანაგრამი.


# def check_anagram(string1, string2):

#     string1 = string1.replace(" ", "").upper()
#     string2 = string2.replace(" ", "").upper()

#     return sorted(string1) == sorted(string2)


# print(check_anagram("dog", "god"))   
# print(check_anagram("Tbilisi", "London")) 


# დავალება 2.
# დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს.
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს
# მისი რაოდენობა


# def count_occurence(string, character):
#     string=string.lower()
#     character=character.lower()
#     return string.count(character)

# print(count_occurence("New York","n"))
# print(count_occurence("Tbilisi",  "n"))
# print(count_occurence("New York",string="London", string="Boston",string="Tbilisi", character= "n"))  - ესე ერთ ლაინად დაწერა პრინტში შეიძლება?
#                                       თუ ცალ-ცალკე უდნა დაიპრინტოს ყოველ ჯერზე?