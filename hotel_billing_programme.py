guests = [
    {'name': 'Rahul', 'days':3, 'room':2500, 'food':1100},
    {'name': 'Priya', 'days':5, 'room':3000, 'food':1800},
    {'name': 'Amit', 'days':2, 'room':2000, 'food':900},
    {'name': 'Sneha', 'days':7, 'room':3500, 'food':2500},
]

#Guest's Individual Totals

for guest in guests:
  guest ['total'] = (guest['room'] + guest ['food']) * guest ['days']
  print (guest['name'], round(guest['total'],2))

print ()

#Guest's Individual Taxes

tax_rate = 0.10
for guest in guests:
  guest['tax'] = guest ['total'] * tax_rate
  print (guest['name'], guest['tax'])

print ()

#Individual Guest's Grand Total

for guest in guests:
  guest['final_bill']=  guest ['total'] + guest['tax']
  print (guest['name'],  round(guest['final_bill'],2))

print ()

#Grand Total (Amount of all guests)

grand_total = 0

for guest in guests:
    grand_total = grand_total + guest['final_bill']

print('Grand Total:', round(grand_total,2))

#Average Billing

average_billing = grand_total / len(guests)
print ('Average Billing:', round(average_billing,2))

#Highest Final bill

highest_bill =0

for guest in guests:
  if guest['final_bill'] > highest_bill:
    highest_bill = guest['final_bill']
    highest_guest = guest['name']
print ('Highest Bill:',  highest_guest,round(highest_bill,2))

lowest_guest_bill = guests[0]['final_bill']
lowest_guest = guests[0]['name']

for guest in guests:
  if guest['final_bill'] < lowest_guest_bill:
    lowest_guest_bill = guest['final_bill']
    lowest_guest = guest ['name']
print ('Lowest Bill:', lowest_guest, round(lowest_guest_bill,2))

#Number of guests currently present

number_of_guests = len(guests)
print ('Number of guests:',number_of_guests )

#Daily Billing Summary

print ()

print ('Number of guests:',number_of_guests )
print ('Grand Total:', round(grand_total,2))
print ('Highest Bill:',  highest_guest,round(highest_bill,2))
print ('Lowest Bill:', lowest_guest, round(lowest_guest_bill,2))
print ('Average Billing:', round(average_billing,2))

print ()

name = input ('Name')
found = False
for guest in guests:
  if guest ['name'] ==name:
    print ('Number of days:', guest['days'])
    print ('Amount Before Tax:',round(guest['total'],2))
    print ('Tax:', round(guest['tax'],2))
    print ("Final Bill:", round(guest['final_bill'],2))
    found = True
if not found: 
    print ('Guest Not Found')
