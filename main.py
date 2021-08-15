from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import *

# Initiate Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "G4654hjggsaSD5dasksdlkasd"
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Grab current date
today = datetime.date(datetime.now()).strftime("%B %d, %Y")

# Class for a new todo 
class NewTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), unique=True, nullable=False)
    # location = db.Column(db.String(250), unique=False, nullable=True),
    # time = db.Column(db.DateTime, nullable=True, unique=False),
    # notes = db.Column(db.String(250), nullable=True, unique=False),

    def __init__(self, task):
        self.task = task


class NewGoal(db.Model):
    # Table that contains an id as well as a goal and date to mark when started and accomplished.
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(250), unique=True, nullable=False)
    date_started = db.Column(db.DateTime, nullable=True)
    date_finished = db.Column(db.DateTime, nullable=True)


    def __init__(self, goal):
        self.goal = goal
        self.date_started = today

# Run once to create the tables
# db.create_all()  

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form.get('new_todo')
        if task == '':
            return redirect(url_for('todo'))
        new_task = NewTask(task)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('todo'))

    all_tasks = db.session.query(NewTask).all()
    if len(all_tasks) == 0:
        message = 'No Current Tasks'
        return render_template('index.html', date=today, message=message)
    return render_template('index.html', date=today, all_tasks=all_tasks)

@app.route('/add_goal', methods=['GET', 'POST'])
def add_new_goal():
    if request.method == 'POST':
        goal = request.form.get('new_goal')
        new_goal = NewGoal(goal)
        db.session.add(new_goal)
        db.session.commit()
        return redirect(url_for('todo'))
        
    all_goals = db.session.query(NewGoal).all()
    return render_template('index.html', goals=all_goals)

@app.route('/delete/<int:task_id>')
def delete_todo(task_id):
    task = NewTask.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(debug=True)
