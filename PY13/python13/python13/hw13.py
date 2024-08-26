დავალება 1.

დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მასში ჩაწერს 1000 ხაზს(ტექსტს არ აქვს მნიშვნელობა)
თავისი ნუმერაციით, შემდეგ წაიკითხეთ ეს ფაილი და დაბეჭდეთ ხაზების რაოდენობა, თუ რამდენია შევსებული.


with open("hello World".txt, '+r') as file:
    for line in range(1, 1001):
        file.write(f'Line {i}\n')
        lines = file.readlines()
    print(f'Total number of lines: {len(lines)}')


    დავალება 2.

დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მეორე, მერვე, მეათე, მეცამეტე და მეჩვიდმეტე ხაზებზე ჩაწერს ამ რიცხვებს შესაბამისი ტექსტური სახელით.

file_name = 'writable_line.txt'


with open(file_name, 'w') as writable_file:
    for line in range(1, 21):
        if line in (2, 8, 10, 13):
            writable_file.write(f'{line}\n')
with open(file_name, 'r') as readable_file:
    lines = readable_file.readlines()
    print(f'Total number of lines: {len(lines)}')

    


დავალება 3.

დაწერეთ პითონის პროგრამა, რომელიც წაიკითხავს ორ ფაილს და მათ გაერთიანებულს ჩაწერს ახალ ტექსტურ ფაილში. გაერთიანებული ფაილი წაიკითხეთ და დაბეჭდეთ ტერმინალში.


def combine_files(text1_file1, text2_file2, combined_text):

   
        with open(text1_file1, '+r') as file1:
            content1 = file1.read()

        with open(text2_file2, '+r') as file2:
        
            content2 = file2.read()
        combined_content = content1 + '\n' + content2

    
        with open (combined_content, 'w') as final_file:
           final_file.write(combined_content)

        with open(final_file, '+r') as final_file:
            final_content = final_file.read()
            print(final_content)

