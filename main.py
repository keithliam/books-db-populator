import csv
import MySQLdb as db

with open(input('Enter filepath: '), 'r', encoding='Latin-1') as f:
	dataset = list(csv.reader(f))

db = db.connect(host='localhost', user='root', passwd='Amazing!', db='tay_bot')

for i in range(0, int(input('How many books? '))):
	cur = db.cursor()
	try:
		cur.execute("""INSERT INTO book(title, author, category) VALUES (%s,%s,%s)""", (dataset[i][3], dataset[i][4], dataset[i][6]))
		db.commit()
	except:     
		db.rollback()

print("Done!")