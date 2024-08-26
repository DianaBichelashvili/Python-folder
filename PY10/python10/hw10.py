# დავალება 1.

# დაწერეთ პითონის ფუნქცია რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით არჩეული რიცხვებით შევსებულ ლისტს.

# დაწერეთ ფუნქცია, რომელიც ხაზობრივი ძიების გამოყენებით მოიძიებს მოცემულ ლისტში რომელიმე ელემენტს.

# გამოიყენეთ ერთ-ერთი სორტირების ალგორითმი და დასორტირებულ სიაში ელემენტის ძიებისთვის დაწერეთ ბინარული ძიება.


# import random

# def generate_sorted_list():
   
#       random_list = [random.randint(1, 100) for x in range(100)]

#       sorted_list = quick_sort_list(random_list)



#       def linear_search (lst:list, current_index:int, search_element:int):
          
#           if current_index == -1:
#               return -1
#           if lst[current_index]==search_element:
#               return current_index
#           return linear_search(lst, current_index-1, search_element)

# lst2 =[10,43,60,75, 90, 95,100]
# check_element=90
# check_linear_search=linear_search(lst2,len(list)-1, check_element)




# def quick_sort_list (lst:list):
#      length=len(lst)

#      if length <= 1:
#              return lst
#      else:
            
#           pivot = lst.pop()
          
#           greater_numbers=[]
#           lesser_numbers=[]
        
#           for number in lst:
#              if number >= pivot:
#                   greater_numbers.append(number)
#              else:
#                 lesser_numbers.append(number)
       
#           return quick_sort_list(lesser_numbers) + [pivot] + quick_sort_list(greater_numbers)
    

# lst3 =[60,12,11,50, 90, 20,100]
# sorted_list = quick_sort_list(lst3)


# def binary_search (lst:list, low, high, x):
#      if high >= low:
#           mid = (high + low) // 2
#           if lst[mid] == x:
#                 return mid
#           elif lst[mid] > x:
#                 return binary_search(lst, low, mid - 1, x)
#           else: 
#              return binary_search(lst, mid + 1, high, x)
#      else:
#           return -1

# sorted_list = quick_sort_list(lst3)
# result= binary_search (sorted_list,0, len(sorted_list)-1)


# დავალება 2.

# დაწერეთ ლამბდა ფუნქცია, რომელიც დააბრუნებს სამის ჯერად რიცხვებს, ამის შემდეგ დაწერეთ ფუნქცია, 
# რომელსაც ატრიბუტებად გადაეწოდება ლისტი და ლამბდა ფუნქცია, ხაზობრივი ძიების და ლამბდა ფუნქციის დახმარებით 
# შეავსეთ ახალი ლისტი(ინდექსებით) და დააბრუნეთ მოცემული ლისტი.(ფუნქციამ უნდა დააბრუნოს ლისტი, რომელშიც შენახული იქნება სამის ჯერადი რიცხვების ინდექსები)


# number = lambda x: x % 3 == 0

# def check_index (lst, number):
#     index_lst = []
#     for index, value in enumerate(lst):
#         if number(value):
#             index_lst.append(index)
#     return index_lst


# number_list = [1, 3, 4, 5, 6, 7]
# print(number_list)

# index_list = check_index(number_list, number)

# print("Index of multiples of three:", index_list)

