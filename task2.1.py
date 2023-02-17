import csv

img = []

with open('stage3_test.csv', 'r', encoding='utf8') as a:
    reader = csv.DictReader(a, delimiter=',')
    for row in reader:
        if len(row['Images'].split(',')) > 3:
            img.append(row)

with open('images.csv', 'w', encoding='utf8') as f:
    fieldnames = ["Id", "Images", "Title", "Description", "Price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in img:
        writer.writerow(row)





