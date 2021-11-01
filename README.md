# Planner

An application that allows the user to add meals to their cart, add their name and address and returns a receipt of the items along with
a dummy expected time. Built with Python, Flask, JavaScript, CSS, Bootstrap, and SQLite.

## Project Status

This project is currently still in development, User can: add, finish, or remove tasks and goals. Functionality to display finished goal date
as well as display all the current and finished goals is in progress.

## Project Screen Shots

### Front of Card
<img src="https://github.com/CharliePine22/planner/blob/main/planner-screenshot-1.png" alt="Your image title" height='400' width="350"/>

### Back of Card
<img src="https://github.com/CharliePine22/planner/blob/main/planner-screenshot-2.png" alt="Your image title" height='400' width="350"/>

# Installation and Setup Instructions
Clone down this repository. 

## How to use:

To use the application, simply type any tasks you require in the input field. When successful, a message will display the task will be 
added to the list. If the User is done with a task but it is reoccuring, clicking the task will check it off wihtout removing it. If the User
won't be needing that task anymore, click the trash icon to delete the task from the list

At the bottom, there's a button that will flip the card so that the User can focus on long-term goals. Upon hovering over each goal, the goal's start
date will appear as well as the trash icon to remove the goal. If the user clicks the clipboard icon, the goal will be marked as completed and removed from the list.
  
   ### To Initialize the Database
    Uncomment the db.create_all() line of code at line 41 in the main.py file to create the database. 
    This line only needs to run once so you can make it a comment after the first inital file run.
  

### Running the application:
    # Start the Flask development web server
    python manage.py runserver 
    
    # Or run the application through your IDE by right clicking on your screen and
    selecting 'Run Python File in Terminal'

## Reflection

This was my first project using Flask and I wanted to create a todo list that was different from similar applications. Project goals included
creating tasks as well as goals to make it both a short-term and long-term todo list.

Originally, I wanted to make it look like a fridge with a chalkboard on it to for grocery lists, but after researching todo lists, I found that
alot of people create similar applications and wanted to change the way mine ran while still sticking with a todo list. 

The main challenge I ran into during this project was displaying messages that gave the user feedback on the action they took. Originally, I created a dictionary with multiple use cases
but upon reading more Flash documentation, I came upon the flash function. With that, i replaced my dictionary and set up flashes in my code whenever an aciton was completed.
