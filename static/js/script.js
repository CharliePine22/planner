const lis = document.querySelectorAll('#task');
const todoContainer = document.querySelector('.task');
const swap = document.querySelector('#swap');
const goals = document.querySelectorAll('#goal_name');
const dateStarted = document.querySelectorAll('#date_started');
const panel = document.getElementById('panel');
const deleteGoal = document.querySelectorAll('#delete_goal');


// Click the check mark to add a line-through the task
for(let i = 0; i < lis.length; i++) {
    lis[i].addEventListener('click', function() {
        // If there is already a line-through the text, remove it.
        if (lis[i].style.textDecoration == 'line-through') {
            lis[i].style.textDecoration = 'none'
            lis[i].style.color = 'white'
        }
        else {
            // Or else put the line through the text
            lis[i].style.textDecoration = 'line-through'
            lis[i].style.color = 'red'
        }
    }, false)
}

// Flip card back to front
swap.addEventListener('click', function() {
    todoContainer.classList.toggle('show')
    console.log('CLICKED!')
})


// Upon hovering on a goal, darken the background except the goal
for(let i=0; i < goals.length; i++) {
    goals[i].addEventListener('mouseover', function() {
        this.style.zIndex = '2'
        panel.style.display = 'initial'

        // Reveal date started and delete icon upon hovering
        dateStarted[i].style.display = 'block'
        deleteGoal[i].style.display = 'block'
    })

    goals[i].addEventListener('mouseout', function() {
        // Remove the overlay
        this.style.zIndex = 'initial'
        panel.style.display = 'none'

        // Rehide the dates and the delete icon
        dateStarted[i].style.display = 'none'
        deleteGoal[i].style.display = 'none'

        // todoContainer.style.transform = 'scale(1.0)'
    })
    
}


