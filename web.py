from flask import Flask, render_template, request
from CSVReader import CSVReader
from Sorter import Sorter

app = Flask(__name__)


@app.route("/")
def index():
    csvreader = CSVReader("data.csv")
    data = csvreader.get_data()
    return render_template("index.html", data=data)


@app.route("/sort")
def sort():
    csvreader = CSVReader("data.csv")
    data = csvreader.get_data()
    sorter = Sorter()

    direction = request.args.get("dir")

    data = sorter.quicksort(data, "date")
    data = sorter.quicksort(data, "priority")

    if direction == "desc":
        return render_template("index.html", data=data, direction=direction)
    else:
        return render_template("index.html", data=reversed(data), direction=direction)


if __name__ == "__main__":
    app.run(debug=True)
