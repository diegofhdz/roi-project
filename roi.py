
class Investment():
    def __init__(self, income, expenses, total_investment):
        self.monthly_income = income
        self.monthly_expenses = expenses
        self.total_invest = total_investment
        self.monthly_cash_flow = 0
        self.roi = 0

    def calcCashFlow(self, month_income, month_expense):
        self.monthly_cash_flow = month_income - month_expense
        return self.monthly_cash_flow

    def calcROI(self, investment, net_cash_flow):
        annual_net_cash_flow = net_cash_flow * 12
        self.roi = (annual_net_cash_flow/investment)
        return self.roi
    
list_of_investments = []

def runProgram():
    while True:
        investment_user = buildInvestment()


def buildInvestment():
    while user_input =='r':
        total_inv = getInvestment()
        monthly_exp = getExpenses()
        monthly_income = getIncome()

        try:
            total_inv = float(total_inv)
            monthly_exp = float(monthly_exp)
            monthly_income = float(monthly_income)
            user_input = ''
        except TypeError:
            user_input = input("One or more of your values is invalid, to try again enter r or enter any other key to quit.\n").strip().lower()
        
    total_inv = abs(total_inv)
    monthly_exp = abs(monthly_exp)
    monthly_income = abs(monthly_income)

    return Investment(monthly_income, monthly_exp, total_inv)

        
        
def getInvestment():
    total_inv = input(r'Enter the total investment amount. This includes the down payment of the rental property, closing costs, any rehabilitation expenses, and any other expenses on the property.\n')
    return total_inv

def getExpenses():
    month_exp = input(r'Enter total monthly expenses. This inclues taxes, utilities, insurance, property manager salary, repairs, mortgage, vacancy, etc.\n')
    return month_exp

def getIncome():
    monthly_inc = input(r'Enter your monthly income. This should be equal to the rent you plan to charge your tenant.\n')
    return monthly_inc