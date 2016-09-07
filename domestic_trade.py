import csv
with open('domestic_trade.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row



        #raw_input("Plz Enter your SKU ID:")