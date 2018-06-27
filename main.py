import csv
import MySQLdb as db

with open('books.csv', 'r', encoding='Latin-1') as f:
	dataset = list(csv.reader(f))

db = db.connect(host='localhost', user='root', passwd='Amazing!', db='tay_bot')

num = int(input('How many books? '))
i = 0
ii = 0

while i < num and ii < len(dataset):
	if dataset[ii][6] == 'Teen & Young Adult':
		cur = db.cursor()
		try:
			cur.execute("""INSERT INTO book(title, author, category, image) VALUES (%s,%s,%s,%s)""", (dataset[ii][3], dataset[ii][4], dataset[ii][6], dataset[ii][2]))
			db.commit()
		except:     
			db.rollback()
		i += 1
	ii += 1

print("Done!")