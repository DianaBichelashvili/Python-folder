# დავალება 1.

# გამოიყენეთ  titanic.csv 

# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “survived.csv” და ჩაწერეთ მხოლოდ გადარჩენილების ინფორმაცია.



# import csv

# with open ("titanic.csv", "r") as file:
#     titanic_reader = csv.Dictreader(open("titanic.csv", "r"))
#     passengers = list(titanic_reader)
#     for row in titanic_reader:
#             print(row["Survived"] )


            
# დავალება 2.

# გამოიყენეთ organizations-100.csv

# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “sorted_csv.csv” და ჩაწერეთ დასორტირებული ინფორმაცია, დაასორტირეთ თანამშრომელთა რაოდენობის მიხედვით



# import csv

# with open ("organization-100.csv", "r") as file:
#       organizations_reader = csv.DictReader(open("organization-100.csv", "r"))
#       sorted_list = sorted(organizations_reader, key=lambda x: int(x["Employees"]), reverse=True)
#       with open("sorted_csv.csv", "w", newline='') as sorted_file:
#         sorted_writer = csv.DictWriter(sorted_file, fieldnames=organizations_reader.fieldnames)
#         sorted_writer.writeheader()
#         sorted_writer.writerows(sorted_list)
    
    
# დავალება 3.

# გამოიყენეთ organizations-100.csv

# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “ssl_companies.csv” და ჩაწერეთ მხოლოდ აიდი, კომპანიის სახელი, ვებ საიტი, ინდუსტრია და დასაქმებულების
# რაოდენობა ისეთი კომპანიების რომელთაც აქვთ ssl-ით დაცული ვებსაიტი(HTTPS)


# import csv

# with open ("organization-100.csv", "r") as file:
#       organizations_reader = csv.DictReader(open("organization-100.csv", "r"))
#       ssl_companies = []
#       for row in organizations_reader:
#             if row["SSL"] == "Yes":
#                 ssl_companies.append(row)
#                 fieldnames = ['id', 'company_name', 'website', 'industry', 'number_of_employees']
#                 updated_list_writer=csv.DictWriter(ssl_companies, fieldnames)
#                 updated_list_writer.writeheader()
#                 updated_list_writer.writerows(ssl_companies)
#                 for row in  organizations_reader:
#                   if row['website'].startswith('https://'):
#                     ssl_companies.append(row)
#                 filtered_row = {key: row[key] for key in fieldnames}
#                 updated_list_writer.writerow(filtered_row)