import random
import json
import csv
import ast
FILENAME = "members.csv"
members = []
print("Surname")
list_surname = []
for x in range(4000):
	list_surname.append(input())
print("Name")
list_name = []
for x in range(4000):
	list_name.append(input())
print("Word")
list_card = []
for x in range(1200):
	list_card.append(input())
for x in range(1000100):
	tel = random.choice(['8903', '8916', '8963', '8905'])
	for x in range(9):
	    tel = tel + random.choice(list('0123456789'))
	mail = ''
	for x in range(7):
		mail = mail + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnm'))
	mail = mail + '@gmail.com'
	data = {"telephone_number" : tel, "mail" : mail}
	print(data)
	month = random.choice(['january','february','march','april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'])
	card = random.choice(list_card)
	card = card + '_' + month +'_'
	for x in range(7):
		card = card +  random.choice(list('0123456789'))
	surname = random.choice(list_surname)
	name = random.choice(list_name)
	member = [name, surname, card, data]
	members.append(member)
with open(FILENAME, "w") as file:
    writer = csv.writer(file)
    writer.writerows(members)
