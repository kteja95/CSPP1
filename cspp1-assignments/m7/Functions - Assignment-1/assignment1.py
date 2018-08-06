''' THE PROGRAM PRINTS THE CREDIR CARD STATEMENT FOR A YEAR'''

def payingDebtOffInAYear(balance, annualInterestRate, monthlyPaymentRate):
	''' CALCULATING NTERST RATES AND PRINTING THE ANNUAL PRINCIPAL'''
	for i in range(12):
		monthlyInterestRate = annualInterestRate/12.0
		minMonthlypayment = monthlyPaymentRate*balance
		monthlyUnpaidbalance = balance - minMonthlypayment
		balance = monthlyUnpaidbalance+(monthlyInterestRate*monthlyUnpaidbalance)
	print(round(balance,2))

	
def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	print(payingDebtOffInAYear(data[0],data[1],data[2]))

if __name__== "__main__":
	main()

