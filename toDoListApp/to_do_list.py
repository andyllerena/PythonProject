from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['Post'] )

def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('home'))

@app.route('/edit/<int:task_id>')
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        return render_template('edit.html', task_id = task_id, task = tasks[task_id])
    else:
        return redirect(url_for('home'))

@app.route('/update/<int:task_id>', methods = ['Post'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = request.form['task']
    return redirect(url_for('home'))

        
if __name__ == '__main__':
    # Starts the Flask application with debug mode on.
    app.run(debug=True)