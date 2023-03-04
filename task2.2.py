import csv

prs = []
with open('stage3_test.csv', 'r', encoding='utf8') as a:
    reader = csv.reader(a)
    for row in reader:
        if row[4] == 'Price':
            pass
        elif 10000 < float(row[4]) < 50000:
            prs.append(row)

with open('price.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    for row in prs:
        writer.writerow(row)