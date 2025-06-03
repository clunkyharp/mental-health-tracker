from flask import Flask, render_template, request, redirect
from models import init_db, insert_entry, get_entries
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # работает на Linux/macOS



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
    dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%d %B %Y, %H:%M")

if __name__ == '__main__':
    app.run(debug=True)


