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
        rootUrl = request.form.get('rootUrl')
        if rootUrl:
            result = webScraper.printStats(rootUrl)
            result = json.dumps(result)
            loaded_r = json.loads(result)
            print (loaded_r)
            return jsonify(result=result)

        else:
            return jsonify(result='Input needed')

    return render_template('index.html')

if __name__ == "__main__":
    app.debug=True
    app.run()