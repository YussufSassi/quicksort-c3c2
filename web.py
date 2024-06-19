from flask import Flask, render_template, request, jsonify
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

    data = sorter.quicksort(data, "priority")

    if direction == "desc":
        data = reversed(data)
        return jsonify(data=list(data), direction=direction)
    else:
        return jsonify(data=data, direction=direction)


if __name__ == "__main__":
    app.run(debug=True)
