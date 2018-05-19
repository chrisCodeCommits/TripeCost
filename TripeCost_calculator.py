'''
Trip cost calculator
************************
b21_ptCost = petrol cost
b22_lpkm = l/100km
b23_trvl = traveled km
************************
'''


b21_ptCost = 14
b22_lpkm = 10
b23_trvl = 30

tripeCost = (b23_trvl/(100/b22_lpkm))*b21_ptCost

print (tripeCost)
