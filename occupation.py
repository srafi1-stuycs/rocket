import csv
import random

occupation_dict = {}

def read_csv():
    with open('occupations.csv', 'rU') as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] == "Job Class":
                continue
            occupation_dict[row[0]] = float (row[1])

def ret_rand():
    keys = occupation_dict.keys()
    rand = random.random() * occupation_dict['Total']
    #print rand
    for key in keys:
        if key == "Total":
            continue
        rand -= occupation_dict[key]
        if rand <= 0:
            return key
    return 0;


read_csv()
print occupation_dict

print ret_rand()
