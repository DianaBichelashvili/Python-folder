# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც წაიკითხავს ფაილს, დაბეჭდეთ ის ხაზები, რომელიც არის ერთმანეთის პალინდრომი


# def is_palindrome(string):
#     string = string.lower()  
#     string="".join(string.split ".")
#     return string == string[::-1]  

# def print_palindromes_from_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             for line in file:
#                 line = line.strip()  
#                 if is_palindrome(line):
#                     print(line)
#     except FileNotFoundError:
#         print(f"file '{filename}'not found")
#     except Exception as e:
#         print(f"Error: {e}")

# print_palindromes_from_file('input_file.txt')


# დავალება 2.

# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტად მიიღებს ფაილის სახელს, წაიკითხეთ ფაილი, დაყავით ხაზები რაოდენობის მიხედვით და ჩაწერეთ ახალ ფაილებში,
# თითოში მაქსიმუმ 10 ხაზი.


# import csv

# def create_file(input_filename, lines_per_file=10):
#     with open(input_filename, 'r', ) as file:
#             reader = csv.reader(file)  
      
#             lines = []

#             for line in reader:
#                 lines.append(line)
            
#                 part_number = 1
#                 if len(lines) >= lines_per_file:
#                     output_filename = f'{input_filename}_part{part_number}.csv'
#                     with open(output_filename, 'w', newline='') as file:
#                         writer = csv.writer(file)
#                         writer.writerows(lines)
                    
#                     part_number += 1
#                     lines = [] 

#             if lines:
#                 output_filename = f'{input_filename}_part{part_number}.csv'
#                 with open(output_filename, 'w', newline='') as file:
#                     writer = csv.writer(file)
#                     writer.writerows(lines)



# create_file('input_file.csv', 10)


# დავალება 3.

# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტებად მიიღებს ფაილის სახელებს, წაიკითხეთ ერთი ფაილი, 
# ამოშალეთ ცარიელი ხაზები და სრული ინფორმაცია ჩაწერეთ მეორე ფაილში.
# def delete_empty_lines(input_file, output_file):
    
#         with open(input_file, 'r') as file:
#             lines = file.readlines()
        
    
#         non_empty_lines = [line for line in lines if line.strip()]

#         with open(output_file, 'w') as outfile:
#             outfile.writelines(non_empty_lines)
        
#         print(f"ცempty lines deleted {output_file}")



# delete_empty_lines('input.txt', 'output.txt')

# დავალება 4.

# დაწერეთ პითონის აპლიკაცია რომელიც დასაწყისისთვის csv ფაილში ჩაწერს შემდეგ ინფორმაციას:


# import csv

# books = [
#     {"title": "1984", "author": "George Orwell", "year": 1949},
#     {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
#     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
#     {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
#     {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
#     {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
#     {"title": "Ulysses", "author": "James Joyce", "year": 1922},
#     {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
#     {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
#     {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
# ]

# def write_to_csv(filename, data):
    
#         with open(filename, 'w', newline='') as csvfile:
#             fieldnames = ['title', 'author', 'year']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
#             writer.writeheader()  
#             writer.writerows(data)  
#             print(f"Data written to {filename}")
           
# write_to_csv('books.csv', books)    



