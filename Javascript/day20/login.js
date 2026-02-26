const btn1 = document.getElementById('btn1');
const sidebar = document.getElementById('sidebar');
const closebtn = document.getElementById('closebtn');
// i need transition effect for sidebar slide in and slide out


btn1.addEventListener('click', () => {
     sidebar.style.display = 'block';
     sidebar.style.right = '0';
     btn1.style.transition = '5s';

});

closebtn.addEventListener('click', () => {
    closebtn.style.transition = '5s';
    sidebar.style.display = 'none';
    sidebar.style.right = '-300px';
    

});
