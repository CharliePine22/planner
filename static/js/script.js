const lis = document.querySelectorAll('#task');
const check = document.querySelectorAll('#finished')
const todo_container = document.querySelector('.task');

// Click the check mark to add a line-through the task
for(let i = 0; i < lis.length; i++) {
    check[i].addEventListener('click', function() {
        if (lis[i].style.textDecoration == 'line-through') {
            lis[i].style.textDecoration = 'none'
        }
        else {
            lis[i].style.textDecoration = 'line-through'
        }
    }, false)
}

// Flip card to display clicked task
for(let i = 0; i < lis.length; i++) {
    lis[i].addEventListener('click', function() {
        todo_container.classList.toggle('show')
        console.log(lis[i])
    })
}
