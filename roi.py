#Diego Hernandez

list_of_investments = []

class Investment():
    def __init__(self, income, expenses, total_investment, name):
        self.monthly_income = income
        self.monthly_expenses = expenses
        self.total_invest = total_investment
        self.name = name
        self.monthly_cash_flow = income - expenses
        self.roi = self.calcROI(total_investment, self.monthly_cash_flow)

    def calcROI(self, investment, net_cash_flow):
        annual_net_cash_flow = net_cash_flow * 12
        roi = round(float(annual_net_cash_flow/investment), 4) * 100
        return roi
    
def runProgram():
    while True:
        print('\n')
        print(f"Welcome to your investment portal. Your total number of investments is {len(list_of_investments)}.")

        if len(list_of_investments) > 1:
            total_roi = 0
            for inv in list_of_investments:
                total_roi += inv.roi

            avg_roi = total_roi/len(list_of_investments)
            print(f"Currently, the average roi on your investments is {avg_roi:.2f}%", '\n')
        
        print('------------')
        print('Menu Options')
        print('New investment - n\nView Current ROIs - v\nQuit - q')
        user_choice = input("What would you like to do?\n").strip().lower()
        if user_choice == 'q':
            break
        elif user_choice != 'n' and user_choice != 'v':
            print("Invalid choice. Try again.")
            continue
        elif user_choice == 'n':
            new_inv = buildInvestment()
            if new_inv != 0:
                list_of_investments.append(new_inv)
                print('\n')
                print(f"Added to investment portfolio, calculated ROI for this investment is {(new_inv.roi):.2f}%")
        elif user_choice == 'v':
            if len(list_of_investments) > 0:
                print('\n')
                for x in enumerate(list_of_investments):
                    print(f"Investment {x[0]}:", x[1].name,  f"- {(x[1].roi):.2f}%")
            else:
                print('\nNo current investments.')


def buildInvestment():
    user_input = 'r'
    while user_input =='r':
        total_inv = getInvestment()
        monthly_exp = getExpenses()
        monthly_income = getIncome()

        try:
            total_inv = float(total_inv)
            monthly_exp = float(monthly_exp)
            monthly_income = float(monthly_income)
            user_input = ''
        except ValueError:
            user_input = input("One or more of your values is invalid, to try again enter r or enter any other key to quit.\n").strip().lower()
            return 0

    total_inv = abs(total_inv)
    monthly_exp = abs(monthly_exp)
    monthly_income = abs(monthly_income)
    inv_name = input('\nWhat is the name for your investment?: ')

    return Investment(monthly_income, monthly_exp, total_inv, inv_name)

        
def getInvestment():
    total_invest = input('\nEnter the total investment amount. This includes the down payment of the rental property, closing costs, any rehabilitation expenses, and any other expenses on the property.\n')
    return total_invest

def getExpenses():
    month_exp = input('\nEnter total monthly expenses. This inclues taxes, utilities, insurance, property manager salary, repairs, mortgage, vacancy, etc.\n')
    return month_exp

def getIncome():
    monthly_inc = input('\nEnter your monthly income. This should be equal to the rent you plan to charge your tenant.\n')
    return monthly_inc



if __name__=="__main__":
    runProgram()