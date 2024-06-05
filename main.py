from Sorter import Sorter
from datetime import datetime
from CSVReader import CSVReader

sorter = Sorter()

csvreader = CSVReader("data.csv")


sorted_bugs = sorter.quicksort([x[0] for x in csvreader.get_data()])


print(sorted_bugs)
