from flask import Flask, render_template, request
from datetime import datetime, timedelta
import csv
import os

app = Flask(__name__)
DATA_FILE = "arbeitszeit.csv"

def calculate_end_time(start_str):
    fmt = "%H:%M"
    try:
        start_dt = datetime.strptime(start_str, fmt)
        pause = timedelta()
        end_dt = start_dt + timedelta(hours=8)
        if end_dt - start_dt >= timedelta(hours=9):
            pause = timedelta(minutes=45)
        elif end_dt - start_dt >= timedelta(hours=6):
            pause = timedelta(minutes=30)
        return start_dt + timedelta(hours=8) + pause
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    end_time = ""
    remaining = ""
    kommt = ""
    if request.method == "POST":
        kommt = request.form.get("kommt")
        now = datetime.now()
        end_dt = calculate_end_time(kommt)
        if end_dt:
            end_time = end_dt.strftime("%H:%M")
            diff = end_dt - now
            remaining = str(diff).split(".")[0] if diff.total_seconds() > 0 else "✅ Arbeitszeit erfüllt!"
            # optional: speichern
            if not os.path.exists(DATA_FILE):
                with open(DATA_FILE, "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Datum", "Kommt", "Ende"])
            with open(DATA_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.today().strftime("%Y-%m-%d"), kommt, end_time])
    return render_template("index.html", kommt=kommt, end_time=end_time, remaining=remaining)

if __name__ == "__main__":
    app.run(debug=False)
