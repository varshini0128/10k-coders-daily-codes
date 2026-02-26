// promises:
// promises are used to handle asynchronous operations in JavaScript.
// It is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

// types of promise:
// 1. pending
// 2. resolved
// 3. rejected


let promise=new Promise((resolve,reject)=>{
    let sucess=true
    if(sucess){
        resolve("successful")
    }
    else{
         reject()
    }
})
promise.then((res)=>{
console.log(res)
}).catch((rej)=>{
    console.log(rej);
})


function demo(a,b){
    return new Promise((resolve, reject)=>{
        if( typeof a == "number" && typeof b == "number"){
            resolve("sucessfully operation is done",[a,b])

        }
        else{
             reject("wrong input")
        }
    })
}

// demo(1,"hi").then(([a,b])=>{
//         console.log(a+b);
//     })
//     .catch((err)=>{
//         console.log(err);
//     })

// setTimeOut is a function that is used to execute a function after a specified time interval.
// it takes two parameters: a callback function and a time interval in milliseconds.

// setTimeout(()=>{
//     console.log("hello world");
// },2000)



// check if the number is negative or positive
// if negative reject by using promise else reslove? 
function checkNumber(num) {
    return new Promise((resolve, reject) => {
        if (num >= 0) {
            resolve("Number is Positive");
        } else {
            reject("Number is Negative");
        }
    });
}

checkNumber(-5)
    .then(result => console.log(result))
    .catch(error => console.log(error));

console.log("--------------------------------")
// print the 1 to 5 with one second gap by using the
// promise chaining?

// function printNumber(num) {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             console.log(num);
//             resolve();
//         }, 1000);
//     });
// }

// printNumber(1)
//     .then(() => printNumber(2))
//     .then(() => printNumber(3))
//     .then(() => printNumber(4))
//     .then(() => printNumber(5));

// print the 5 to 1 with one second gap by using the
// promise chaining?


function printNum(num) {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(num);
            resolve();
        }, 1000);
    });
}

printNum(5)
    .then(() => printNum(4))
    .then(() => printNum(3))
    .then(() => printNum(2))
    .then(() => printNum(1));








































function demo(a){
    let p=new Promise((resolve,reject)=>{
        if(a==10){
            resolve('program running')
            for (let i=1;i<=a;i++){
                 console.log(i);
             }
        }
        else{
            reject('rejected because of wrong input')
        }
    }).then((resolve)=>{
        console.log(resolve);
    
    }).catch((reject)=>{
        console.log(reject);
    })
    
}
// demo(10)
demo('hi')













function addition(a,b){
    let p = new Promise((resolve, reject) => {
        if(isNaN(a) || isNaN(b)){
             reject('wrong')
            
        }else{
           resolve('right')
        }
    })
}

addition(1,10).then((res)=>{
    console.log(res);
}).catch((rej)=>{
    console.log(rej);
})











