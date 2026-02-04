let back=document.getElementById("btn1")
let forward1=document.getElementById("btn2")
let img=document.querySelector("img")
let images=[
        "./i1.png",
        "./i2.png",
        "./image.png"
];

img.style.height='300px'
img.style.width='500px'
let index=0
forward1.addEventListener("click",()=>{
    index++
    if(index>=images.length){
        index=0
    }
    img.src=images[index]
})

back.addEventListener("click",()=>{
    index--
    if(index<0){
        index=images.length-1  
    }
    img.src=images[index]
  
})