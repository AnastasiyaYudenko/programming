import csv

with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=',')
    with open('without2.csv', 'w', encoding='utf8') as a:
        writer = csv.DictWriter(a, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            del row["Images"]
            del row["Description"]
            writer.writerow(row)
