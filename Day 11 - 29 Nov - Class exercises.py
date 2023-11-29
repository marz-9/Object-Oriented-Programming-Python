class Numbers:
    def __init__(self):
        self.numbers=[]
    def add_num(self, num):
        self.numbers.append(num)
    def sum_numbers(self):
        summ=0
        for i in self.numbers:
            summ+=1
        return summ
n1=Numbers()
n1.add_num(1)
n1.add_num(3)
print(n1.sum_numbers())



class Library:
    def __init__(self):
    #We defined it as class to minimize the amount of coding lines, so that one dictionary
    #can save a list within the library list(which will create nested list)
        self.library=[]
    def add_book(self, title,author, copies):
        book={"Title":title,"Author":author,"Copies":copies}
        self.library.append(book)
    def display_books(self):
        for i in self.library:
            print(i)
    def search_book(self,title):
        
        for i in self.library:
            if (i["Title"] == title):
                print(i["Author"])
            elif (i["Title"] != title):
                print("No book with this title available")
lb1=Library()
lb1.add_book("Python","Fatma",10)
lb1.add_book("C++","John",10)
lb1.add_book("Java","John",10)
lb1.display_books()
lb1.search_book("C++")

print()

class BankAccount:
    def __init__(self, account,balance):
        self.__account=account
        self.__balance=balance
    def get_account(self):
        print("Your account number is: {}. The balance: {}.".format(self.__account, self.__balance))
    def Deposit(self,deposit):
        try:
            self.__deposit=deposit
            if (self.__deposit>0):
                d_total= self.__balance+self.__deposit
                return d_total
            else:
                return "Please enter correct amount"
        except Exception as exc1:
            print("error: ",type(exc1),str(exc1))   
    def Withdraw(self,withdraw):
        self.__withdraw=withdraw
        w_total= self.__balance-self.__withdraw
        return w_total

ba1=BankAccount(1234567891234, 5000)
ba1.get_account()

print("After deposit: ", ba1.Deposit(0))
print("After withdraw: ", ba1.Withdraw(500))
