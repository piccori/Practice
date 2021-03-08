import csv

nobel_winners = [
    {'category': 'physics',
     'name': 'Albert Einstein',
     'nationality': 'Swiss',
     'sex': 'male',
     'year': 1921},
    {'category': 'physics',
     'name': 'Paul Dirac',
     'nationality': 'British',
     'sex': 'male',
     'year': 1933},
    {'category': 'chemistry',
     'name': 'Marle Curie',
     'nationality': 'Polish',
     'sex': 'female',
     'year': 1911}
]


with open('nobel_winners.csv', 'w') as f:  # 本ではmodeが'wb'であったが'w'でOK
    fieldnames = nobel_winners[0].keys()
    fieldnames = sorted(fieldnames)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)

with open('nobel_winners.csv')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
