from flask import Flask, render_template, redirect, request
from database import create_tables, get_timelines, get_contacts


app = Flask(__name__)

app.config['SECRET_KEY'] = "sjdgfwkjnfiu24hro2nfiuwbfjwkbrj2h3br2"


@app.route('/')
def home_page():
    images = [
        "https://pbs.twimg.com/media/EtYsVfLU0AUgj9x?format=png&name=900x900",
        "https://c4.wallpaperflare.com/wallpaper/853/430/473/naruto-windows-backgrounds-wallpaper-preview.jpg",
        "https://branditechture.agency/brand-logos/wp-content/uploads/wpdm-cache/Deathnote-900x0.png",
        "https://i.pinimg.com/originals/91/16/e1/9116e130d3307064ec1bc9aa7f4c97d8.jpg",
        "https://logowik.com/content/uploads/images/one-punch-man4479.logowik.com.webpцц"
    ]
    return render_template('index.html', images=images)

@app.route('/timeline')
def timeline_page():
    articles = get_timelines()
    return render_template(template_name_or_list='timeline.html', timelines=articles)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    articles = get_contacts()
    return render_template(template_name_or_list='contact.html', contacts=articles)


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

