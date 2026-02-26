// callback hell is a situation where we have multiple nested callbacks and it becomes difficult to read and maintain the code. 
// It is also known as pyramid of doom.

function register(){
    setTimeout(()=>{
        console.log("registered")
    },5000)

}

function login(){
    setTimeout(()=>{
        console.log("loged in");
    },3000)
}

function home(){
    setTimeout(()=>{
        console.log("welcome to home page");
    },2000)
}

register(()=>{
    login(()=>{
        home(()=>{
            console.log("all functions are executed");
        })
    })
})

// callback hell can be avoided by using promises and async/await.
// async function is a function that is declared with the async keyword
//  and it always returns a promise.
// await is a keyword that is used to wait for a promise to resolve or reject.
//  It can only be used inside an async function.
async function demo(){
    await register();
    await login();
    await home();
    console.log("all functions are executed");
}
// callback hell def:
// Callback hell is a situation where we have multiple nested callbacks and it becomes difficult to read and maintain the code.
//  It is also known as pyramid of doom. It occurs when we have multiple asynchronous operations that depend on each other, and we end up with a lot of nested callbacks. This can make the code difficult to read and understand, and it can also lead to errors if we are not careful with the order of execution. To avoid callback hell, we can use promises or async/await to handle asynchronous operations in a more structured way.
// callback function def:
// A callback function is a function that is passed as an argument to another function and is executed after the parent function has completed its execution.

// promise chaining def:
// Promise chaining is a technique where we can chain multiple promises together to avoid callback hell. It allows us to execute multiple asynchronous operations in a sequential manner. Each promise returns a new promise, which can be used to chain the next operation. This way, we can avoid nested callbacks and make our code more readable and maintainable.

