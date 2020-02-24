from flask import Flask, render_template, url_for, request


# NLP Packages


# Web Scrapping Packages
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

# Home Route 

# Compare Route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_summary')
def index():
    return render_template('compare_summary.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)