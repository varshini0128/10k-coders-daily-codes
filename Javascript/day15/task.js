// p=prompt("enter a number")
// b1=document.getElementById("btn1");
// b1.addEventListner("click",()=>{
//     b=document.body
//     for (let r=1; r<=10;r++){ 

//         b.writeln(`${p} * ${r} = ${p*i}`)
//     }
// })
// // multiplication table of given number using button and input box
//         console.log(`${k} * ${r} = ${k*r}`);
// }
let input=document.createElement("input")
input.type="number"
input.id="inp1"
body.appendChild(input)
let button=document.createElement("button")
button.id="btn1"
button.textContent="click me"
body.appendChild(button)
button.addEventListener("click",()=>{
    b=document.body
    let val=document.getElementById("inp1").value
    for (let r=1; r<=10;r++){
        let val1=document.createElement("p")
        val1.textContent=`${val} * ${r} = ${val*r}`
        b.appendChild(val1)
    }

})