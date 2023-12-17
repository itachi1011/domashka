from flask import Flask, render_template, redirect, request

app = Flask(__name__)

app.config['SECRET_KEY'] = "sjdgfwkjnfiu24hro2nfiuwbfjwkbrj2h3br2"


@app.route('/')
def index_page():
    return render_template('index.html ')

@app.route('/servie')
def service_page():
    return render_template('service.html')


@app.route('/team')
def team_page():
    return render_template('team.html')

@app.route('/why')
def why_page():
    return render_template('why.html')

@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)