let display=document.getElementById('display')
let div1=document.getElementById('div1')
let datedisplay=document.getElementById('datedisplay')
let daydisplay=document.getElementById('daydisplay')

let date=new Date()
let hr=date.getHours()
let min=date.getMinutes()
let sec=date.getSeconds()
let days=['Sun','Mon','Tue','Wed','Thurs','Fri','Sat']
let months=['Jan','Feb','March','April','May','June','July','August','September','October','November','December']
let h;
let m;
let s;

// console.log(hr);
h=hr<10?'0'+hr:hr
m=min<10?'0'+min:min
s=sec<10?'0'+sec:sec
display.textContent=`${h}:${m}:${s}`

let day1
let month
let year
let day2
function display1(){
    date=new Date()
    hr=date.getHours()
    min=date.getMinutes()
    sec=date.getSeconds()
    day1=date.getDate()
    day2=date.getDay()
    month=date.getMonth()
    year=date.getFullYear()
    h=hr<10?'0'+hr:hr
    m=min<10?'0'+min:min
    s=sec<10?'0'+sec:sec
    display.textContent=`${h}:${m}:${s}`
    daydisplay.textContent=`${days[day2]}`
    datedisplay.textContent=`${day1}/${months[month]}/${year}`
}
display1()
console.log(display1());

setInterval(display1,1000)

