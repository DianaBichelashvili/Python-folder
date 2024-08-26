# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით დაგენერირებული ელემენტისგან შემდგარ ლისტს, 
# გამოიყენეთ sort() მეთოდი და sorted() ფუნქცია, დააბრუნეთ დასორტირებული ლისტი ჯერ ზრდადობით და შემდეგ კლებადობით


# import random

# def generate_sorted_list():
   
#     random_list = [random.randint(1, 100) for x in range(100)]

#     sorted_list = sorted(random_list)
#     sorted_list = sorted(random_list, reverse=True)

#     return sorted_list


# დავალება 2.

# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით დაგენერირებული ელემენტისგან შემდგარ ლისტს,
# გამოიყენეთ ორი სორტირების ალგორითმი(არ აქვს არსებითი მნიშვნელობა, რომელი ალგორითმები იქნება), 
# ერთი ალგორითმით დაასორტირეთ ზრდადობით, მეორე ალგორითმით დაასორტირეთ კლებადობით, ორივე შედეგი დაპრინტეთ ტერმინალში. 

# import random

# def selection_sort_list():
   

#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#         lst[i], lst[min_index] = lst[min_index], lst[i]


# lst = [random.randint(1, 100) for x in range(100)]
# selection_sort_list (lst)
# print (lst) 


# კლებადობით
# def selection_sort_list():


#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i+1, len(lst)):
#             if lst[j] > lst[min_index]:
#                 min_index = j
#         lst[i], lst[min_index] = lst[min_index], lst[i]

   
# lst = [random.randint(1, 100) for x in range(100)]
# selection_sort_list (lst)
# print (lst) 





# def quick_sort_list (lst:list):
#       length=len(lst)

#       if length <= 1:
#             return lst
#       else:
            
#          pivot = lst.pop()
          
#          greater_numbers=[]
#          lesser_numbers=[]
        
#          for number in lst:
#             if number >= pivot:
#                  greater_numbers.append(number)
#             else:
#                  lesser_numbers.append(number)
       

#          return quick_sort_list(lesser_numbers) + [pivot] + quick_sort_list(greater_numbers)
    

# lst = [random.randint(1, 100) for x in range(100)]
# lst_increase = quick_sort_list(lst)
# print (lst_increase)


# klebadobit

# def quick_sort_list (lst:list):
#       length=len(lst)

#       if length <= 1:
#             return lst
#       else:
            
#          pivot = lst.pop()
          
#          greater_numbers=[]
#          lesser_numbers=[]
        
#          for number in lst:
#             if number <= pivot:
#                  greater_numbers.append(number)
#             else:
#                  lesser_numbers.append(number)
       

#          return quick_sort_list(greater_numbers) + [pivot] + quick_sort_list(lesser_numbers)
    

# lst = [random.randint(1, 100) for x in range(100)]
# lst_decrease = quick_sort_list(lst) 
# print (lst_decrease)


# დავალება 3.

# ქალაქში მოსახლეობის რაოდენობა ყოველ წელს იზრდება 2 პროცენტით. 

# 1.დაწერეთ ფუნქცია რომელიც გამოთვლის, რამდენი წლის შემდეგ იქნება მოსახლეობა 10000 ადამიანზე მეტი.

# 2. დაწერეთ ფუნქცია რომელიც ატრიბუტად მიიღებს წლების რაოდენობას, დააბრუნეთ მოსახლეობის რაოდენობა ამდენი წლის შემდეგ.


# def years_population (population, increase_percentage):
#     years = 0
#     increased_population = initial_population
#     initial_population=10000
#     increase_percentage=2

#     while population < increased_population:
#         population *= (1 + increase_percentage/ 100)
#         years += 1

#     return years

# 2.
# def population_after_years(years, initial_population, increase_percentage):
#     years = 5
#     population = initial_population
#     increase_percentage=2
#     initial_population=10000

#     for x in range(years):
#         population *= (1 + increase_percentage / 100)

#     return int(population)  


# future_population = population_after_years()

# დავალება 4. 

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს 2, ინტეჯერებისგან შემდგარ, ლისტს, შეადარეთ ერთი და იგივე ადგილზე 
# მდგომი ელემენტები და დააბრუნეთ ახალი ლისტი, რომელშიც მოცემული იქნება შედარების შედეგად მიღებული მაღალი რიცხვები. დაამატეთ ლოგიკური გამონაკლისი შემთხვევები.



# def compare_lists(list1, list2):
#     result = []
    
#     if len(list1) != len(list2):
#         return result
    
#     for i in range(len(list1)):
#         if list1[i] == list2[i]:
#             result.append(list1[i])
    
#     return result


# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 4, 5, 5]

# result = compare_lists(list1, list2)
# print(result)


# დავალება 5.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს 3 რიცხვს, ფუნქციას დააბრუნებინეთ პასუხი, არის თუ არა შესაძლებელი ამ რიცხვებით სამკუთხედის აგება.
# სამკუთხედის ორი გვერდის ჯამი, მეტია მესამე გვერდზე



# def check_triangle(a, b, c):

#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False


# result = check_triangle()
# print(result)



# დავალება 6.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს სტუდენტების ლისტს,
# student_list = [
#     '1 - Melissa Parker - 91 60 89 84 26',
#     '2 - Paige Simon - 39 90 38 74 49',
#     '3 - Kevin Atkins - 27 7 89 96 62',
#     '4 - Barry Ramos - 94 93 62 30 66', 
#     '5 - Karen Hudson - 51 15 94 20 8',
#     '6 - Jennifer Diaz - 56 31 81 52 50', 
#     '7 - Robin Smith - 90 3 92 86 14', 
#     '8 - Kevin Clark - 69 65 47 58 44', 
#     '9 - Lisa Shields DDS - 92 1 53 40 89', 
#     '10 - John Kennedy - 21 41 12 15 90', 
# ]

# გამოთვალეთ თითოეული სტუდენტისთვის საშუალო ქულა და დააბრუნებინეთ ფუნქციას ლისტის სახით, 
# [[name, avg], [name, avg] …]

# def calculate_average_scores(student_list):
#     result = []
    
#     for student_info in student_list:
#         elements = student_info.split(' ')
        
       
#         name_lst= elements[1] 
#         scores_lst = elements[2]  
        
#         scores = list(map(int, scores_lst.split()))
        
 
#         average_score = sum(scores) / len(scores)
    

#         student_updated_info = zip(name, average_score) აქ ზიპის გამოყენება შემეძლო? 
        
#         result.append(student_updated_info)
    
#     return result



# final_list= calculate_average_scores(student_updated_info)
# print(final_list)



# დავალება 7.

# დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეწოდება ლისტი:
# [9255, 1358, 1045285, 59828218, 881525, 388, 8586, 9988, 599828, 812358, 855, 85585, 85885, 888]

# დააბრუნეთ ახალი ლისტი, რომელიც შედგება რიცხვებისგან:
# 	შეიცავს 5, 8 ციფრებს
# 	ციფრი 8-ს რაოდენობა არის 5-ის რაოდენობაზე მეტი


# def filter_numbers(nums):
#     result = []
    
#     for num in nums:
#         num_str = str(num)
#         count_5 = num_str.count('5')
#         count_8 = num_str.count('8')
        
#         if (len(num_str) == 5 or len(num_str) == 8) and count_8 > count_5:
#             result.append(num)
    
#     return result


# numbers = [9255, 1358, 1045285, 59828218, 881525, 388, 8586, 9988, 599828, 812358, 855, 85585, 85885, 888]
# filtered_numbers = filter_numbers(numbers)
# print(filtered_numbers)