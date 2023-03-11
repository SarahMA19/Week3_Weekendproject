class return_on_investment():
     user_input_income = {}  
     user_input_expenses ={}
     user_input_investment ={}

     
     def get_value(self, prompt):
          while True:
               try:
                    v = int(input(prompt))
                    if v >= 0:
                         break
                    else:
                         print("Your value needs to be greater than 0")
               except:
                    print("Sorry, I need a vaild number")
          return v
     
          
     
     def cash_flow(self):
          income = (sum(self.user_input_income.values()))
          expenses = (sum(self.user_input_expenses.values()))
          return income - expenses
         

     def ROI(self):
          investment = (sum(self.user_input_investment.values()))
          yearly =  self.cash_flow() * 12
          print(yearly)
          return yearly / investment * 100
          
          

     def income(self):
          while True:
               print("\nLet's figure out your total income from this property!")
     
               
               
               rental_income = self.get_value("\nWhat is your monthly rental income on the property? :$")
               laundry = self.get_value("\nWhat is your laundry income for the month? :$"))
               storage = self.get_value("\nWhat is your storage unit income for the month? :$"))


               self.user_input_income.update({
                    "rental income": rental_income, 
                    "laundry" : laundry,
                    "storage":storage
               })

               end = input("\nThank you for answering all our income questions! Need to add anything else? (Y/N)")
               if end == "N":
                    print("\nHere is your total monthly income $" + str(sum(self.user_input_income.values())))
                    break
          

     def expenses(self):
          while True:
               print("\nLet's figure out your total expenses of this property!")
               insurance =self.get_value("\nHow much do you pay for each month on insurance? :$"))
               tax = self.get_value("\nHow much do you pay in taxes each month? :$"))
               utilites = self.get_value("\nHow much do you pay in monthly utilites? :$"))
               repairs = self.get_value("\nHow much would you like to set aside for repairs each month? :$"))
               property_managment = self.get_value("\nWhat do you pay your property manager each month? :$"))
               morgatage = self.get_value("\nHow much is your monthly morgage? :$"))
               vacancy = self.get_value("\nHow much would you like to set aside for vacancy each month? :$"))

               self.user_input_expenses.update({
               "insurance": insurance,
               "tax": tax,
               "utilies": utilites,
               "repairs" : repairs,
               "property management": property_managment,
               "morgatage" : morgatage,
               "vacancy" : vacancy
               })

               end = input("\nThank you for answering all our expenses questions! Need to add anything else (Y/N)")
               if end == "N":
                    print("\nHere is your total monthly expenses $" + str(sum(self.user_input_expenses.values())))
                    break
               

     def investment(self):
          while True:
               print("\nLet's figure out your total investment into this property!")
               down_payment = self.get_value("\nHow much do you pay for the down payment on this property? :$"))
               closing_costs = self.get_value("\nHow much were the closing costs :$"))
               fix_budget = self.get_value("\nHow much did you need to spend on fixing the place up prior to renting? :$"))

               self.user_input_investment.update({
                    "down_payment": down_payment,
                    "closing_cost": closing_costs,
                    "fix_budget" : fix_budget 
               })

               end = input("\nThank you for answering all our investment questions! Need to add anything else (Y/N)")
               if end == "N":
                    print("\nHere is your total investment expenses $" + str(sum(self.user_input_investment.values())))
                    break
               



     def run(self):
          self.income()
          self.expenses()
          self.investment()
          while True:
               resp = input("\nWelcome, lets start calculating your ROI for your rental property. Type 'c' for total cash flow, type 'r' for cash on cash ROI")
               if resp.lower() == "c":
                    print("Here is your cash total cash flow:" + str(self.cash_flow()))
               elif resp.lower() == "r":
                    print("This is your ROI for this rental property %" + str(self.ROI()))
                    




home = return_on_investment()
home.run()
