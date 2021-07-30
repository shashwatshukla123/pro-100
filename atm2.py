class Atm2:
    def __init__(self,atmcardnumber,pinnumber):
        self.atmcardnumber = atmcardnumber
        self.pinnumber = pinnumber

    def withdrawl(self,amount):
        new_money = 100000 - amount
        print("You have withdrawn amount: "+str(amount) +". Your remaining balance is: "+ str(new_money))

    def check_balance(self):
        print("Your balance is 100000")
    
    
def main():

    pin_number  = input("enter your pin number:- ")
    card_number = input("insert your card number:- ")
        
    new_user =  Atm2(card_number,pin_number)

    print("1.Check Balance   2.Withdrawl")
    activity = int(input("enter your activity number :- "))
    
    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")
    
if __name__ == '__main__':
   main()
    

