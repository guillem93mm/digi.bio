import csv
from statistics import mean, stdev

'''
Program created by Guillem Martinez to open, calculate and transfer stats into a newly created file.
This is the 6th exercise of the Tech Assignment by Digi.Bio.
'''
def main():

    # First I open the file and then I read it
    file_A = open('csv_A.csv')
    csvreader = csv.reader(file_A)

    # Extract first row
    first_row = []
    first_row = next(csvreader)

    # Extract data
    data = next(csvreader)
    # Convert strings to number in the data list. From the data list, I have excluded test6 (null value).
    # This is why I have sliced the list to contain only the first 5 values.
    data_numbers = [float(x) for x in data[:5]]

    # Closing files = good practise
    file_A.close()

    # Calculate mean and stdv. (I also created a dictionary containing both values)
    data_avg = mean(data_numbers)
    deviation = stdev(data_numbers)
    statistics = {'mean': data_avg, 'stdeviation': deviation}
    print(statistics)

    # Create a new csv file and store the statistics. 
    # csv.writer directly controls line endings. Therefore I add nothing as a newline
    # to prevent a new empty row in between.
    with open('csv_B.csv', 'w', newline='') as createdfile:
        writer = csv.DictWriter(createdfile, fieldnames=statistics.keys())
        writer.writeheader()
        writer.writerow(statistics)

main()
