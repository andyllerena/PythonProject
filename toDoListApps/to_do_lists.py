from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

# Initialize the database
def initialize_database():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    tasks = Task.query.order_by(Task.id).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['task']
    new_task = Task(content=task_content)

    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    except:
        return 'There was an issue adding your task'

@app.route('/delete/<int:id>')
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('home'))
    except:
        return 'There was a problem deleting that task'

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['task']

        try:
            db.session.commit()
            return redirect(url_for('home'))
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('edit.html', task=task)

if __name__ == '__main__':
    initialize_database()  # Initialize the database
    app.run(debug=True)

