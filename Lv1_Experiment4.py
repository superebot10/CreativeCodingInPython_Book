total = input('What is the total on the bill?: ')
tip = input('What % tip would you like to give?: ')
people = input('How many people are sharing the bill?: ')
people = int(people)
tip = int(tip)
total = int(total)
tip_amount = total * tip / 100
print('Tip amount = ', tip_amount)
total_bill = tip_amount + total
print('Total bill = ', total_bill)
print('---------------------------------------')
print('Tip amount per person: ', tip_amount / people)
print('Total amount per person: ', total_bill / people)
#test123