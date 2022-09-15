import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_connection():
    connection = sqlite3.connect('data_base/example.sqlite3')
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/best_selling/<int:count>')
def get_best_selling_tracks(count):
    connection = get_connection()
    tracks = connection.execute('SELECT * FROM best_selling_tracks').fetchmany(count)
    connection.close()
    return render_template('best_tracks.html', tracks=tracks)









app.run(debug=True, port=5050)