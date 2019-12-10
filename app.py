from flask import *
from flask import render_template
from scraper import webScraper

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

app = Flask(__name__)

@app.route('/', methods= ["GET", "POST"])
def homepage():
    if request.method == 'POST':
        symbol = request.form.get('rootUrl')
        rootUrl = 'https://www.msn.com/en-us/money/stockdetails/analysis?symbol='+symbol
        if rootUrl:
            result = webScraper.printStats(rootUrl)
            result = json.dumps(result)
            loaded_r = json.loads(result)
            print (loaded_r)
            return jsonify(result=result)

        else:
            return jsonify(result='Input needed')

    return render_template('index.html')

if __name__ == '__main__':
        import os
        port = int(os.environ.get('PORT', 33507))
        app.run(host='0.0.0.0', port=port)

