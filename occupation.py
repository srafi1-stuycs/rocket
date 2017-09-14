import csv

occupation_dict = {}

def read_csv():
    with open('occupations.csv', 'rU') as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for row in reader:
            occupation_dict[row[0]] = row[1]
read_csv()
print occupation_dict
