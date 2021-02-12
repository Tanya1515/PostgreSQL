import random
import json
import csv
FILENAME = "expeditions.csv"
FILENAME1 = "art.csv"
expeditions = []
countries = []
cities = []
art = []
c = []
art_ok = []
cost = 0
count = 0
count_art = 0
for x in range(28):
	art.append(input())
for x in range(3):
	print("Country")
	countries.append(input())
	for y in range(20):
		cities.append(input())
	c.append(cities)
for x in range(1200000):
	country = random.choice(countries)
	print(x)
	for k in range(3):
		if (country == countries[k]):
			y = k
	city = random.choice(c[y])
	name_of_expedition = country+'_'+city
	place = {"country":country, "city":city}
	sql_place = str(place).replace(',','\,').replace('{','"{').replace('}', '}"')
	days = random.randint(10,75)
	if (days>30):
		salary_per_day = random.randint(300,500)
	elif (days>60):
		salary_per_day = random.randint(500,700)
	else:
		salary_per_day = random.randint(100,300)
	for z in range(random.randint(3,15)):
		count = count +1
		member = random.randint(1,900000)
		salary = salary_per_day*days
		print()
		artefacts = []
		for t in range(random.randint(0,3)):
			count_art = count_art + 1
			name_art = random.choice(art)
			cost_of_artefact = random.randrange(3000, 500000, 10)
			premium = cost_of_artefact * 0.1
			artefacts.append(name_art)
			status = random.choice(['Ok', 'Damaged', 'Fragile'])
			epoch = random.choice(['X','XI','I','II','III','V','VI','VII','VIII', 'IX', 'XV', 'XVI', 'XIII'])
			info = {"status":status, "epoch":epoch}
			sql_info = str(info).replace(',','\,').replace('{','"{').replace('}', '}"')
			art_str = str(member) + ',' + name_art + ',' + str(name_of_expedition) + ',' + str(cost) + ',' + str(premium) + ',' + sql_info
			art_ok.append(art_str)
		sql_arr = str(artefacts).replace('[','{').replace(']', '}').replace(', ','\,')
		exp_1 = str(member) + ',' + str(name_of_expedition) + ',' + sql_place + ',' + str(days) + ',' + str(salary_per_day) + ',' + sql_arr  + ',' + str(salary) 
		expeditions.append(exp_1)
with open(FILENAME, "w") as file:
	for z in range(count):
	    	file.write(expeditions[z] + "\n")
with open(FILENAME1, "w") as file:
	for z in range(count_art):
	    	file.write(art_ok[z] + "\n")



















