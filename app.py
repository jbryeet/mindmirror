from flask import Flask, render_template, request
from analysis import analyze_text

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', result=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    user_entry = request.form['entry']
    result = analyze_text(user_entry)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
