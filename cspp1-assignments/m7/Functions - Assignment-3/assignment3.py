''' THE PROGRAM PRINTS THE MINUMUM AMOUNT NEEDED TO CLEAR THE LOAN WITH MORE ACCURATE ALGO'''

def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
def payingDebtOffInAYear(balance, annualInterestRate):
    initBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    low = balance/12.0
    high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
    epsilon = 0.01
    minPay = (high + low)/2.0
    month = 0
    while abs(balance) >= epsilon:
        balance = initBalance
        month = 0
        balance = calculate(month, balance, minPay, monthlyInterestRate)
        if balance > 0:
            low = minPay
        else:
            high = minPay
        minPay = (high + low)/2.0
    minPay = round(minPay,2)
    print('Lowest Payment: ' + str(minPay))


def main():
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1]))
    
if __name__== "__main__":
    main()
