class return_on_investment():
     user_input_income = {}  
     user_input_expenses ={}
     user_input_investment ={}

     #created a function to test each input for a vaild number, more orgazined this way than a while loop for each input line
     def get_value(self, prompt):
          while True:
               try:
                    v = int(input(prompt))
                    if v >= 0:
                         break
                    else:
                         print("\nYour value needs to be $0 or greater")
               except:
                    print("\nSorry, I need a vaild number")
          return v
     
          
     #cash flow calcualtion
     def cash_flow(self):
          income = (sum(self.user_input_income.values()))
          expenses = (sum(self.user_input_expenses.values()))
          return income - expenses
         
     #ROI caluclation
     def ROI(self):
          investment = (sum(self.user_input_investment.values()))
          yearly =  self.cash_flow() * 12
          print(yearly)
          return yearly / investment * 100
          
          
     #dictonary within a function - seemed cleaner to then call the function in my run function
     def income(self):
          while True:
               print("\nWelcome, I would like gather some information about your rental property in order to calcuate your ROI. Let's start with your total income from this property!")
     
               rental_income = self.get_value("\nWhat is your monthly rental income on the property?:$")
               laundry = self.get_value("\nWhat is your laundry income for the month?:$")
               storage = self.get_value("\nWhat is your storage unit income for the month?:$")


               self.user_input_income.update({
                    "rental income": rental_income, 
                    "laundry" : laundry,
                    "storage":storage
               })

               end = input("\nThank you for answering all our income questions! Do you need to go back and add a different $$$ value? (Y/N)")
               if end == "N":
                    print("\nHere is your total monthly income $" + str(sum(self.user_input_income.values())))
                    break
          
     #dictonary within a function - seemed cleaner to then call the function in my run function
     def expenses(self):
          while True:
               print("\nNow, let's get your total expenses of this property!")
               insurance =self.get_value("\nHow much do you pay for each month on insurance?:$")
               tax = self.get_value("\nHow much do you pay in taxes each month?:$")
               utilites = self.get_value("\nHow much do you pay in monthly utilites?:$")
               repairs = self.get_value("\nHow much would you like to set aside for repairs each month?:$")
               property_managment = self.get_value("\nWhat do you pay your property manager each month?:$")
               morgatage = self.get_value("\nHow much is your monthly morgage?:$")
               vacancy = self.get_value("\nHow much would you like to set aside for vacancy each month?:$")

               self.user_input_expenses.update({
               "insurance": insurance,
               "tax": tax,
               "utilies": utilites,
               "repairs" : repairs,
               "property management": property_managment,
               "morgatage" : morgatage,
               "vacancy" : vacancy
               })

               end = input("\nThank you for answering all our expenses questions! Do you need to go back and add a different $$$ value? (Y/N)")
               if end == "N":
                    print("\nHere is your total monthly expenses $" + str(sum(self.user_input_expenses.values())))
                    break
               
     #dictonary within a function - seemed cleaner to then call the function in my run function
     def investment(self):
          while True:
               print("\nFinally, let's gather your total investment into this property!")
               down_payment = self.get_value("\nHow much do you pay for the down payment on this property?:$")
               closing_costs = self.get_value("\nHow much were the closing costs:$")
               fix_budget = self.get_value("\nHow much did you need to spend on fixing the place up prior to renting?:$")

               self.user_input_investment.update({
                    "down_payment": down_payment,
                    "closing_cost": closing_costs,
                    "fix_budget" : fix_budget 
               })

               end = input("\nThank you for answering all our investment questions! Do you need to go back and add a different $$$ value? (Y/N)")
               if end == "N":
                    print("\nHere is your total investment expenses $" + str(sum(self.user_input_investment.values())))
                    break
               



     def run(self):
          self.income()
          self.expenses()
          self.investment()
          while True:
               resp = input("\nNow that I have all your informaion, let's calculate your cash on cash ROI for the rental property. Type 'c' for total cash flow, type 'r' for cash on cash ROI")
               if resp.lower() == "c":
                    print("Here is your total cash flow:$" + str(self.cash_flow()))
               elif resp.lower() == "r":
                    print("Here is your cash on cash ROI for this rental property: %" + str(self.ROI()))
                    

home = return_on_investment()
home.run()
