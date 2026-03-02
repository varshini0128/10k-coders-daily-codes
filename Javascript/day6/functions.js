// functions :
// it is a block of code which is used to perform specific task
// functions for the code reusability

for (let i=1;i<=10;i++){
    console.log(i);
    
}

// types of functions:
// --------------------

// 1. named function or pure function
// ----------------------------------
// the function with name
// syntax:
// function functionname(parameters){
//     //statements
// })


function greet(){
    console.log('good morning');
}

greet()

function sum(a,b){
    console.log(a+b);
}
 
sum(2,9)

// function with less parameters and more arguments
// function add(a,b){
//     console.log(a+b);
//     console.log(arguements);
//     console.log(arguements[4],arguements[2],arguements[3]);
    
// }
// add(1,20,30,40,50)
// extra values are stored in arguements 

function demo(){
    return 'hello'
}
console.log(demo);

// this keyword is used to access global var in functional scope
let a=100
function demo1(){
    let a=20
    console.log(a);//20
    
    console.log(this.a);//80
    
}
console.log(demo1);


// hoisting:
// calling a function before its declaration
greet()
function greet(){
    console.log('good morning');
}

// hoisting is possible in named functions


// prototype of a function
// copy of an function is known as prototype
greet()
function greet(){
    console.log('good morning');
}

let a1 = new greet()
console.log(a1);
// console.log('prototype' in a );
console.log(Object.getPrototypeOf(a)==greet.prootype);


// 2. anonymous function
// the function without name 
// syntax:
// function(){
//statements 
// }

let b=function (name){
    console.log('happy new year', name);
    
}
b('ajay')


console.log('-------------');

// functions with more parameters nd less arguements
let b1= function(a,b,c,d){
    console.log(a-b);
    console.log(c-d);
}
b1(3,1)

// function with less parametters and more arguements
let b2= function(a,b){
    console.log(a-b);
    // console.log(c-d);
    console.log(arguments);
    console.log(arguements[3]);
}
// b2(3,1,4,5,6,7)


// function with return keyword

let greet1 = function(){
    return 'hello world'
}
console.log(greet1());

// console.log(a3)
// function with this keyword
let b5='hi'
let a3 =function (){
    var b5='hi'
    console.log(b5);
    console.log(this.b5,'----');
    console.log(window.b5,'----');
}
console.log(a3())

// hoisting is not possible for this anonymous function



// prototype

let a9=function (){
console.log("hi hoisting");
}
// console.log("prototype" in a);

let b9=new a9()
console.log(Object.getPrototypeOf(b9) == a9.prototype);

// 3. generator function
function * demo3(){
    console.log('hi');
    // return 'hi'
    yield 1
    yield 2
    yield 1+3

    
}
let p=demo3()
p.next()
console.log(a.next());
console.log(a.next());
console.log(a.next());
 
console.log(a.next().value);
console.log(a.next().value);
console.log(a.next().value);
console.log(a.next().value);
console.log(a.next().done);


// function with parameters

function * add(a,b){
    yield 'sum of two numbers'
    yield a+b
}
let m=add(1,2)
console.log(m.next().value);
console.log(m.next().value);