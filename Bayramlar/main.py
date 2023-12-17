from flask import Flask, render_template


app = Flask(__name__)

app.config['SECRET_KEY'] = "sjdgfwkjnfiu24hro2nfiuwbfjwkbrj2h3br2"

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/yangi')
def yangi_page():
    return render_template('yangi_yil.html')

@app.route('/ram')
def ram_page():
    return render_template('ramazon.html')

@app.route('/eid')
def eid_page():
    return render_template('eid.html')

@app.route('/nowrooz')
def now_page():
    return render_template('nowrooz.html')

if __name__ == '__main__':
    app.run(debug=True)