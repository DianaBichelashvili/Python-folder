# დავალება 1.

# მოცემულია სია my_list:
# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
# დაწერეთ პროგრამა, რომელიც შეკრებს ამ სიის მე–3, მე–9 და მე–14 ელემენტებს და მიღებულ შედეგ დაბეჭდავს ტერმინალში.




# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

# index_list = [3, 9, 14]

# sum_numbers = 0

# for index in index_list:
#     sum_numbers += mylist[index]

# print("Sum of numbers on index 3, 9, and 14:", sum_numbers)

# დავალება 2.

# შექმენით 20 რენდომ რიცხვისგან შემდგარი ლისტი, შექმენით ახალი ლისტი, რომელშიც შეინახავთ პირველი ლისტიდან 
# მხოლოდ კენტ მნიშვნელობებს და დაბეჭდეთ ლისტში ყველაზე მცირე და ყველაზე დიდი ელემენტი. არ გამოიყენოთ ფუნქციები min() და max()


# from random import randint 

# Random_numbers= randint (1,21)

# odd_list = [i for number in Random_numbers if number%2!=0]


# print (Random_numbers)
# print (odd_list)

# odd_list_2 = odd_list.copy()
# print (odd_list_2.sort() )
# print (odd_list_2.sort(reverse=True) )

# or 
# Random_numbers= randint (1,21)

# odd_list_2=[]
# for i in Random_numbers:
#   if i%2 !=0:
#      odd_list_2.append(i)

# print (Random_numbers)
# print (odd_list_2)



# დავალება 3.

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს
# შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს
# d. შექმენით ახალი ლისტი my_llist_2 , რომელსაც ექნება my_llist მნიშვნელობა, გაასუფთავეთ my_llist_2 
# მნიშნველობა და დაბეჭდეთ my_llist და my_llist_2 ლისტები


# my_llist = [43, '22', 12, 66, 210, ["hi"]]

# index_210 = my_llist.index(210)
# hello_list= my_list.append("hello")
# updated_list=my_list.remove(2)
# print (updated_list)

# my_llist_2 = my_llist.copy()
# cleared_list=my_llist_2.clear()
# print (my_llist)
# print (cleared_list)



# დავალება 4.

# დაწერეთ პროგრამა, რომელიც დაბეჭდავს ორი მატრიცის ჯამს, ჯამი გამოითვლება შემდეგი წესით,
# ერთი და იგივე ადგილზე მდგომი ელემენტები ემატება ერთმანეთს, მატრიცების განზომილებები უნდა იყოს ერთი და იგივე

# matrix_rows=3
# matrix_columns=3

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]


# sum_matrix = [
#     [matrix1[i][j] + matrix2[i][j] for j in range(matrix_columns)]
#     for i in range(matrix_rows)
# ]


# print("matrix sum is:")
# for row in sum_matrix:
#     print(row)


#     დავალება 5.

# დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას, ტრანსპონირება ნიშნავს ინდექსების შებრუნებას,
# მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3], ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე


# matrix_rows = 3
# matrix_columns = 3

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix_2 = [
#     [matrix1[j][i] for j in range(matrix_rows)]
#     for i in range(matrix_columns)
# ]


# print("matrix:")
# for row in matrix1:
#     print(row)

# print("matrix2:")
# for row in matrix_2:
#     print(row)

   
   
#    დავალება 6.



# list comprehension გამოყენებით შექმენით რენდომ რიცხვებისგან შემდგარი 4x4 კვადრატული მატრიცა

# from random import randint

# matrxi_rows = 4
# matrix_columns = 4

# matrix = [[randint(1, 100) for j in range(matrix_columns)] for i in range(matrix_rows)]

# print("matrix:")
