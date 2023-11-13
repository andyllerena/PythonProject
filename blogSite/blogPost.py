from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

blog_posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        date = datetime.now()
        post = {'title': title, 'body': body, 'date': date}
        blog_posts.append(post)  # Corrected variable name to blog_posts
        return redirect(url_for('home'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)



