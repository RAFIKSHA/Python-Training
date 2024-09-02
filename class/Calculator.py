class Calculator:
     def put_data(self):
          
          self.num1=int(input("enter the number1"))
          self.num2=int(input("enter the number2"))
          
     def add(self):
          print("addition=",self.num1+self.num2)
     def sub(self):
          
          print("substraction=",self.num1-self.num2)
     def mul(self):
          print("multiplication=",self.num1*self.num2)
     def div(self):
          print("division=",self.num1/self.num2)

c=Calculator()
while True:
    yes_no=input("continue yes/no")
    if yes_no=="yes":
        c.put_data()
        ch=int(input("enter your choice\n 1.add:\n2.sub\n3.mul\n4.div :"))
        if ch==1:
            c.add()
        elif ch==2:
            c.sub()
        elif ch==3:
            c.mul()
        elif ch==4:
            c.div()
        else:
            print("enter valid choice")
    else:
            print("thank you")
            break



     