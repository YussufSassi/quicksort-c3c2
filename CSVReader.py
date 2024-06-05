import csv
from datetime import datetime


class CSVReader:
    def __init__(self, filename):
        self.filename = filename
        self.bugs = []

    def get_data(self):
        with open(self.filename, newline="") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in csvreader:
                cleaned_row = [x.strip("\\t") for x in row]

                bug_date_timestamp = int(
                    datetime.strptime(cleaned_row[1], "%Y-%m-%d").strftime("%s")
                )
                bug_id = cleaned_row[0]

                self.bugs.append((bug_date_timestamp, bug_id))
            return self.bugs
