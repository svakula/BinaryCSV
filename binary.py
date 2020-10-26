import itertools
import csv
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in itertools.product([0,1], repeat=16):
        formstr = str(i).replace("(","").replace(")","").replace(",","")
        writer.writerow(formstr)