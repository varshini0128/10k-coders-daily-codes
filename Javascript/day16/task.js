
let body = document.body
let h2=document.querySelector('h2')
let h1=document.getElementById("h1")
inp1.addEventListener('keypress',(event)=>{
    let r = Math.floor(Math.random()*255)
    let g = Math.floor(Math.random()*255)
    let b = Math.floor(Math.random()*255)
    body.style.backgroundColor=`rgb(${r},${g},${b})`
    h1.textContent=event.key
    h2.textContent=event.charcode
})

let b=document.getElementById('b')

b.addEventListener('mouseleave',()=>{
        b.style.backgroundColor='black'
        b.style.color='white'
})
b.addEventListener('mouseover',()=>{
        b.style.backgroundColor='lightblue'
          b.style.color='black'
})
