import collections
import csv

with open('stage3_test.csv', 'r', encoding='utf-8') as a:
    csvreader = csv.reader(a, delimiter=',', quotechar='"')
    counter = collections.Counter()
    for word in csvreader:
        if word[2]:
            counter[word[2]] += 1
    max = counter.most_common(20)
    min = counter.most_common()[-21:-1]
    print("20 самых частотных: ", max)
    print("20 самых редких: ", min)

