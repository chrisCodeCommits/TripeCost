'''
Trip cost calculator
************************
b21_ptCost = gaz cost
b22_lpkm = l/100km
b23_trvl = traveled km
************************
'''


from decimal import Decimal


b0 = input('Enter (in numbers) the gaz cost per liter:')
b21_ptCost = int(b0)

currency = input('Enter your currency sign:')

b01 = input('Enter (in numbers) the car fuel consumption (100km/l):')
b22_lpkm = int(b01)

b02 = input('Enter (in numbers) the the km distance you want to travel:')
b23_trvl = int(b02) 


tripeCost = (b23_trvl/(100/b22_lpkm))*b21_ptCost
convFloat_to_Dc = Decimal(tripeCost)
lim_to_2 = round(convFloat_to_Dc,2)

strConv = str(lim_to_2)


print ('**** '+'This trip will cost you '+currency+' '+ strConv+' ****')
