import csv

with open('Find_Link.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

    ref = ''
    for row_num, data in enumerate(rows):
        ref += data[row_num]
    print(ref)
