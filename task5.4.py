import csv
import collections

with open('stage3_test.csv', 'r', encoding='utf-8') as a:
    csvreader = csv.DictReader(a, delimiter=',', quotechar='"')
    dict = {}
    for row in csvreader:
        dict[row["Id"]] = row["Price"]

    ordered_dict = collections.OrderedDict(sorted(dict.items(), key=lambda product: product[1]))
    print(ordered_dict)

    ordered_dict_reverse = collections.OrderedDict(sorted(dict.items(), key=lambda product: product[1], reverse=True))
    print(ordered_dict_reverse)