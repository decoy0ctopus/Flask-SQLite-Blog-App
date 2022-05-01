import sqlite3
import pandas as pd
import json
from flask import Flask, render_template
import plotly
import plotly.express as px

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(r'database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    # Load the data into a DataFrame
    posts_df = pd.read_sql_query("SELECT * from posts", conn)
    conn.close()
    fig = px.bar(posts_df, x="id", y="title", barmode="group")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', posts=posts, graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(host='0.0.0.0')