'''
Created on Mar 19, 2020

@author: marbe
'''
import csv

'''
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ';') # read file with different delimiter
'''


# regular reader
'''                                            # read file and write it into new
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # next(csv_reader)  # skips first line
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=';')
        
        for line in csv_reader:
            csv_writer.writerow(line)
'''
    
# dictionary reader
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    
#    for line in csv_reader:
#        print(line)
#        print(line['email'])        # only email 
    
    
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name','last_name','email']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=';')

        csv_writer.writeheader()
        
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
    
    
'''
    # iterates over the 3 column
    for line in csv_reader:
        print(line[2])
''' 
    