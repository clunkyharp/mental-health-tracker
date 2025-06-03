from flask import Flask, render_template, request, redirect
from models import init_db, insert_entry, get_entries
from datetime import datetime



app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        situation = request.form['situation']
        worry = request.form['worry']
        anxiety_level = int(request.form['anxiety_level'])
        insert_entry(situation, worry, anxiety_level)
        return redirect('/history')
    return render_template('index.html')

@app.route('/history')
def history():
    entries = get_entries()
    return render_template('history.html', entries=entries)

@app.template_filter('format_datetime')
def format_datetime(value):
    months = {
        '01': 'января', '02': 'февраля', '03': 'марта',
        '04': 'апреля', '05': 'мая', '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября',
        '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    day = dt.day
    month = months[dt.strftime("%m")]
    year = dt.year
    time = dt.strftime("%H:%M")
    return f"{day:02d} {month} {year}, {time}"

if __name__ == '__main__':
    app.run(debug=True)


