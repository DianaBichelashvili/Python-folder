
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

#პრინტის მეთოდი , რომ დავინახოთ რა მონაცემები არის შეყვანილი ლინკდლისტი
#ორი მეთოდი იწერება ერთ დროულად
#ჯერ არის append და შემდეგ გამოჩენის მეთოდი print 
#append - ამატებს ლისტის ბოლო ელემენტს
#append ის დროს ვამატებთ ახალ მონაცემს, რომელიც ატრიბუტად გადაეცემა აფენდს

def append(self, new_data):
      new_node = Node(new_data)# აფენდის განხორციელებისას ვქმნით ახალ ნოუდს.
      if self.head is None: #აქ მოწმდება სად ჩაჯდა ახალი ნოუდი, თუ ჰედი არ გვაქვს
        self.head = new_node   #ჰედი უნდა გახდეს ახალი ნოუდი
        return 
      
      #ქვემოთ უკვე ძიებას იწყებს ბოლო ელემენტიდან/
      # თუ გვაქვს ჰედი,  მაშინ უნდა მოვიძიოთ ბოლო ელემენტი
      #ბოლო ელემენტი არის ჰედი ამასთანავე და ნექსთიც ნანი იქნება რადგან ამავე დროს ბოლოა
      # თუ ბოლო ელემენტს გააჩნია ნექსთი მაშინ ვანიჭებთ ნიუ მოუდს და ვაილის მეშვეობით ვამოწმებთ სანამ მაქვს ნექსთი გააჩნია . შესაბამსისად ბოლო ელემნტზე არ არის მისული
      
      last_node = self.head

      while(last_node.next):
          last_node = last_node.next
      
      last_node.next = new_node
            
            #აქ აღწერილია ბეჭდვის მეთოდი, 

      def print(self):
         current_node = self.head
    
         while current_node is not None:
            print(current_node.data, end='') #ერთ ხაზზე რომ დაიბეჭდოს ყველა ელემენტი
            current_node = current_node.next #აქ ქერენთ ნოუდი არის ჰედი. მაგრამ დაბეჭდვის შემდეგ გახდება ნექსთი სანამ არ მივა ბოლო ელემენტზე
                                             #მანამ სანამ ვაილი არ გახდება ნანი

      #ინდექსის ამოშლის მეთოდი 
      def remove_at (self, index):
          if index < 0 or self.head is None:
              return
          
          if index == 0:
              self.head = self.head.next    #ამ შემთხვევაში თუ ნოლის ტოლია ჰედი წაიშლება და მისი შემდეგი გახდება ჰედი, თუ ისიც ნოლის ტოლი არ იქნება
              return
          
          current_node = self.head # ჰედი იმიტომ რომ პირველი ელემენტიდან იწყება შემოწმება
          current_position=0 # რადგან პირველი ელემენტი ინდექსში ყოველთვის ნოლზე იმყოფება
          while current_node is not None and current_position < index-1:
              current_node = current_node.next
              current_position += 1

              #აქ სანამ იქნება კონკრეტულ ინდექსზე მანამდე ხორციელდება ვაილი. ეს ორი პირობა  უნდა შესრულდეს რომ ელემნეტის პოვნა განხოციელდეს
              # იმ ობიექტის წინა ელემენტის ვარჩევთ ჯერ და შემდეგ მის მომდევნო ელემენტს ვშლით current_position += 1
              # ქცემოთ ვუთითებთ შემდეგს რომლის წაშლაც გვინდა და ვწერთ რომ ეს შემდეგი გახდეს მისი მომდევნო ელემენტი

              if current_node.next:
                  current_node.next = current_node.next.next 

#value ამოშლის მეთოდi
      def remove_at (self, value)
          if value is not None:
              return
        
          if self.head is None:
              self.head = self.head.next    
              return
          
          current_node = self.head

          current_node= remove_at(current_node)
          while current_node.next and current_node.next.data!= value:
    
              current_node = current_node.next
      
              if current_node.next:
                 current_node.next= current_node.next.next
        





        #Stack - push and pop
     

class Node:
   def __init__(self, data=None):
       self.data=data
       self.next=None
       

class Stack:
          def _init_ (self) #ჰედის მაგივრად აქ ტოპი არის გამოყენებული წინა შემთხვევისგან განსხვავებით
               self.top_node=None
               self.length=0

        #აბრუნებს ცარიელია თუ არა 
def is_empty(self):
          return self.length==0

#რა ინფორმაციის მოცულობაა შეყვანილი სტეკში განსაზღვრავს ეს მეთოდი
def size (self):
   return self.length
  

  # დამატების მეთოდი
def push(self, data):
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

# წაშლის მეთოდი


def pop (self)
     if not self.empty()
     popped_item=self.top_node.data 
     self.top = self.top.next 




     # ეს ქვედა სწორე ლოგიკაა წაშლის?            

def pop2(self):   
     if self.is_empty():
         print("Stack is empty")
         return None
     else:
         popped_node = self.top
         self.top = self.top.next
         popped_node.next = None
         self.length -= 1
         return popped_node.data
    






