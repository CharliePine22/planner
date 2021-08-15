const lis = document.querySelectorAll('#task');
const check = document.querySelectorAll('#finished')
const todo_container = document.querySelector('.task');
const swap = document.querySelector('#swap')

// Click the check mark to add a line-through the task
for(let i = 0; i < lis.length; i++) {
    check[i].addEventListener('click', function() {
        if (lis[i].style.textDecoration == 'line-through') {
            lis[i].style.textDecoration = 'none'
            lis[i].style.color = 'white'
        }
        else {
            lis[i].style.textDecoration = 'line-through'
            lis[i].style.color = 'red'
        }
    }, false)
}

// Flip card to display clicked task
for(let i = 0; i < lis.length; i++) {
    lis[i].addEventListener('click', function() {
        todo_container.classList.toggle('show')
    })
}

// Flip card back to front
swap.addEventListener('click', function() {
    todo_container.classList.toggle('show')
    console.log('CLICKED!')
})