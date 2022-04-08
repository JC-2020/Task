from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls')
    data = json.loads(req.content)
    return render_template('index.html', data=data)