let c=0;
body=document.body
h1=document.getElementById('h1')
b1=document.getElementById('b1')
b2=document.getElementById('b2')

h1.textContent=c

b1.addEventListener('click',()=>{
    c+=1
    h1.textContent=c
})
b2.addEventListener('click',()=>{
    c-=1
    h1.textContent=c
})
// how to hide and show text in input field
inp=document.getElementById('inp')
btn=document.getElementById('btn')
btn.addEventListener('click',()=>{
    if(inp.type==='password'){
        inp.type='text'
        btn1.textContent='Hide'
    }else{
        inp.type='password'
        btn.textContent='Show'
    }           
})