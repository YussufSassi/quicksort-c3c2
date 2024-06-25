import csv
from datetime import datetime


class CSVReader:
    def __init__(self, filename):
        self.filename = filename
        self.bugs = []

    def get_data(self):
        with open(self.filename, newline="", encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in csvreader:
                bug_date_timestamp = int(
                    datetime.strptime(row[1], "%Y-%m-%d").timestamp()
                )
                bug_id = row[0]
                bug_status = row[3]
                bug_priority = row[5]
                bug_affected_users = row[12]
                bug_description = row[4]

                if bug_status == "Neu":
                    bug_status = 0
                elif bug_status == "In Bearbeitung":
                    bug_status = 1
                elif bug_status == "Gelöst":
                    bug_status = 2

                if bug_priority == "Mittel":
                    bug_priority = 0
                elif bug_priority == "Hoch":
                    bug_priority = 1
                elif bug_priority == "Sehr hoch":
                    bug_priority = 2

                self.bugs.append(
                    {
                        "id": int(bug_id),
                        "date": bug_date_timestamp,
                        "status": bug_status,
                        "priority": bug_priority,
                        "affected_users": int(bug_affected_users),
                        "description": bug_description,
                    }
                )
            return self.bugs
