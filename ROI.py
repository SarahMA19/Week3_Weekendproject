
class return_on_investment():
       

       def __init__(self, cash_flow, ROI):
          self.cash_flow = cash_flow
          self.ROI = ROI
        

       def cash_flow(self):
          print("Here is your total monthly income $" + str(sum(user_input_income.values())))
          print("\nHere is your total monthly expenses $" + str(sum(user_input_expenses.values())))
          income = (sum(user_input_income.values()))
          expenses = (sum(user_input_expenses.values()))
          self.cash_flow = income - expenses

       def ROI(self):
          print("Here is your total investment cost $" + str(sum(user_input_investment.values())))
          investment = (sum(user_input_investment.values()))
          yearly = self.cash_flow * 12
          self.ROI = yearly // investment
          print(yearly)
          print(self.ROI)
         

       def run():
           while True:
               resp = input("Welcome, lets start calculating your ROI for your rental property. Type 'i' for income, 'e' for 'expenses' and 'ivest' for investments")
               if resp.lower() != "i" or "e" or "invest":
                    print("\nYou must type correct letter for each selection")
               elif resp.lower() == "i":
                    user_open_1
               elif resp.lower() == "e":
                    user_open_2
               elif resp.lower() == "invest":
                    user_open_3



#*******************      Income Dictionary     ****************
user_input_income = {}
user_open_1 = True
while user_open_1:
     print("Let's figure out your total income from this property!")
     rental_income =int(input("\nWhat is your monthly rental income on the property? :$"))
     laundry =int(input("\nWhat is your laundry income for the month? :$"))
     storage =int(input("\nWhat is your storage unit income for the month? :$"))
     

     user_input_income.update({
          "rental income": rental_income, 
          "laundry" : laundry,
          "storage":storage
     })

     end = input("\nThank you for answering all our income questions! Need to add anything else (Y/N)")
     if end == "N":
          print("\nHere is your total monthly income $" + str(sum(user_input_income.values())))
          break
     elif end == "Y":
          user_open_1


    
#*********       Expenses Dictionary     ***********
user_input_expenses ={}
user_open_2 = True

while user_open_2:
     print("\nLet's figure out your total expenses of this property!")
     insurance =int(input("\nHow much do you pay for each month on insurance? :$"))
     tax = int(input("\nHow much do you pay in taxes each month? :$"))
     utilites = int(input("\nHow much do you pay in monthly utilites? :$"))
     repairs = int(input("\nHow much would you like to set aside for repairs each month? :$"))
     property_managment = int(input("\nWhat do you pay your property manager each month? :$"))
     morgatage = int(input("\nHow much is your monthly morgage? :$"))
     vacancy = int(input("\nHow much would you like to set aside for vacancy each month? :$"))

     user_input_expenses.update({
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
          print("\nHere is your total monthly expenses $" + str(sum(user_input_expenses.values())))
          break
     elif end == "Y":
          user_open_2




          #*********       Total Investment Dictionary     ***********
user_input_investment ={}
user_open_3 = True

while user_open_3:
     print("\nLet's figure out your total investment into this property!")
     down_payment =int(input("\nHow much do you pay for the down payment on this property? :$"))
     closing_costs = int(input("\nHow much were the closing costs :$"))
     fix_budget = int(input("\nHow much did you need to spend on fixing the place up prior to renting? :$"))

     user_input_investment.update({
          "down_payment": down_payment,
          "closing_cost": closing_costs,
          "fix_budget" : fix_budget 
     })

     end = input("\nThank you for answering all our investment questions! Need to add anything else (Y/N)")
     if end == "N":
          print("\nHere is your total investment expenses $" + str(sum(user_input_investment.values())))
          break
     elif end == "Y":
          user_open_3



home = return_on_investment(0,0)
home.run()

          