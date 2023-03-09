// let btn = document.getElementById('btn');
// let red_btn = document.getElementById('red_btn');
// let blue_btn = document.getElementById('blue_btn');
// let green_btn = document.getElementById('green_btn');
// let content = document.getElementById('content');

red_btn.addEventListener('click', () => {
    content.style.background = 'red';
});

blue_btn.addEventListener('click', () => {
    content.style.background = 'blue';
});

green_btn.addEventListener('click', () => {
    content.style.background = 'green';
});

btn.addEventListener('click', () => {
    alert('나 눌렀어?') ;
});