print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? \n '))
tip = int(input('How much tip would you like to give? 10, 12 or 15? \n'))
split = int(input('How many people to split the bill? \n'))

total = bill + bill * tip / 100
total_final = total / split
print('Each person should pay: {:.2f}'.format(total_final)) 