from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///network.db"
db = SQLAlchemy(app)
class Post(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    title = db.Column(db.String(50),nullable = False)
    content = db.Column(db.Text())

    def __repr__(self):
        return f"postid {self.id}, post title {self.title}"

@app.route('/')
def index():
    # db.session.add(Post(id = 1,title = "myfirstpost", content = "content"))
    # db.session.commit()
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/create_post/', methods = ['GET','POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title = title, content = content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_post.html')

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run()