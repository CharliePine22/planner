from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

# Initiate Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "G4654hjggsaSD5dasksdlkasd"
Bootstrap(app)

## CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Grab current date
today = datetime.date(datetime.now()).strftime("%B %d, %Y")

class NewTask(db.Model):
    ## Class for a new todo 
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), unique=True, nullable=False)

    def __init__(self, task):
        self.task = task


class NewGoal(db.Model):
    ## Table that contains an id as well as a goal and date to mark when started and accomplished.
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(250), unique=True, nullable=False)
    date_started = db.Column(db.String(50), nullable=True)
    date_finished = db.Column(db.String(50), nullable=True)


    def __init__(self, goal):
        self.goal = goal
        self.date_started = today

## RUN ONCE TO CREATE THE TABLES IN THE DATABASE
# db.create_all()  

@app.route('/', methods=['GET', 'POST'])
def todo():
    ## Main page that shows all the tasks and goals
    if request.method == 'POST':
        task = request.form.get('new_todo')
         # Check to see if goal already exists in database
        exists = db.session.query(NewTask.id).filter_by(task=task).first() is not None

        if exists:
            flash('That task is already in your list, please try again.')
            return redirect(url_for('todo'))
        if task == '':
            # If the user leaves the input field blank, have them try again
            flash("Can't leave the text field blank, please try again.")
            return redirect(url_for('todo'))
        # Add new task into database
        new_task = NewTask(task)
        db.session.add(new_task)
        db.session.commit()
        flash('Task successfully added!')
        return redirect(url_for('todo'))

    # Grab hold of tasks and goals to display them on screen
    all_tasks = db.session.query(NewTask).all()
    all_goals = db.session.query(NewGoal).all()

    if len(all_tasks) == 0:
        # If there are no current rows in database, display error
        message = 'No Current Tasks'
        return render_template('index.html', date=today, message=message)

    return render_template('index.html', date=today, all_tasks=all_tasks, goals=all_goals)


@app.route('/delete/<int:task_id>')
def delete_todo(task_id):
    ## Grab the id of the task that needs to be deleted and remove it 
    task = NewTask.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task successfully deleted!')
    return redirect(url_for('todo'))


@app.route('/add_goal', methods=['GET', 'POST'])
def add_new_goal():
    ## Add a new goal to the database

    # Find the total number of goals that dont have a finished date
    count = NewGoal.query.filter(NewGoal.date_finished == None).count()

    if count == 3:
        # Limit goals to 3 at a time
        flash('You can only have 3 active goals at one time, erase or complete one to add more!')
        return redirect(url_for('todo'))
    if request.method == 'POST':
        goal = request.form.get('new_goal')
        if goal == '':
            flash("You can't leave the input field blank, please try again.")
            return redirect(url_for('todo'))
        # Check to see if goal already exists in database
        exists = db.session.query(NewGoal.id).filter_by(goal=goal).first() is not None

        if exists:
            # Goal already exists
            flash('That goal is already in the database, please try again!')
            return redirect(url_for('todo'))
        else:
            new_goal = NewGoal(goal)
            db.session.add(new_goal)
            db.session.commit()
            flash('Goal successfully added!')
            return redirect(url_for('todo'))

@app.route('/complete_goal/<int:goal_id>', methods=['GET', 'POST'])
def complete_goal(goal_id):
    # Update the completion date and finish the goal
    goal = NewGoal.query.get(goal_id)
    goal.date_finished = today
    db.session.commit()
    flash('Goal successfully completed!')
    return redirect(url_for('todo'))

@app.route('/delete_goal/<int:goal_id>')
def delete_goal(goal_id):
    ## Delete the goal based on the given id
    goal = NewGoal.query.get(goal_id)
    db.session.delete(goal)
    db.session.commit()
    flash('Goal successfully deleted!')
    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(debug=True)
