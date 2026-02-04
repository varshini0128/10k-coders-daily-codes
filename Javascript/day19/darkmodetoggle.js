let btn1=document.getElementById("btn1")
let body=document.body
// console.log(btn1);

body.style.transition='2s'
btn1.addEventListener("click",()=>{
    if(btn1.textContent=='Dark Mode'){
    body.style.backgroundColor='black'
    body.style.color='white'
    btn1.backgroundColor='white'
    btn1.color='black'
    btn1.textContent='Light Mode'
    
    }else{
        body.style.backgroundColor='white'
         btn1.backgroundColor='black'
        btn1.color='white'
        btn1.textContent='Dark Mode'
        body.style.color='black'
    }
})