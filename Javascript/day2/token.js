// Tokens
// tokens can start with alphabets
// identification rules:
let a2=10       
console.log(a2)


// 1='asd'
// console.log(1)  error variable should not start with number but can contain in between naming variables


a1=90
console.log(a1)
// @k=8
// console.log(@k) cant start with special characters


// can start with _ and $
_s='js'
console.log(_s);
$rate=80
console.log($rate)


// cant define keywords as variables
// keyword ==> predefined words
// if=2
// console.log(if)
// for='python'
// console.log(for)


// cant contain space while defining variable or naming variables
// a 1 = 3
// console.log(a 1);

// datatypes or literals
// Number
// BigInt
let p2=90
console.log(p2,typeof p2)
let k2=2n
console.log(k2,typeof k2)
// range ==> -2^56-1 to 2^56 - 1 number can store out of this range big int is used
let i=Number(8)
console.log(i, typeof i)
let o=BigInt(7)
console.log(o, typeof o)

let v=Number('varsh')
console.log(v,typeof v)


// day2
// string:  string is a collection of characters
// characters can be anything alpha numeric special symbols

// defining the string:
        // 1) by using the single quotations
            let a='this is string'
            console.log(a,typeof a);
        // 2) by using double quotes
            // let b='who's riya' to overcome this we use double quotation
            let b = "who's riya"
            console.log(b,typeof b);
        // 3) by using constructor
            let c=String("domini's daughter")
            console.log(c,typeof c);
        // 4) by using backticks `` for multiple lines
            let d = `hello hi 
                     js world`
            console.log(c,typeof c);


// string concatenation:
        // 1)using '+'
            let f = "flash"
            let k = "man"
            console.log(f+" "+k)
            console.log(f+k)
                // str+int==>str
                    let k1=20
                    console.log('my age is'+k1);


        // 2)using template literals:
        let p=74
        let l=2
        console.log(`multiplication of ${p} and ${l} is ${p*l}`);


// decimals are also considered as number in javascript
let r=20.32
console.log(r,typeof r); 
// float is not a datatype it  also comes under number type 


// boolean data type: 
        // used to check the condition
        // it returns true or false based on the condition


// defining booleans
            // 1)
                let j=true
                console.log(j,typeof j);
            // 2)using boolean constructor
                let q=Boolean(false)
                console.log(q,typeof q)

    // default value for true is 1 and false is 0
                console.log(Number(j),"----true-----");
                console.log(Number(q),"-----false----");
                
let i1=undefined
console.log(i1,typeof i1);

let f1=null
console.log(f1,typeof f1);

let y=NaN
console.log(isNaN(y));

let s2= Symbol("hello")
console.log(s2,typeof s2);

console.log(s2.description ,"its type is",typeof s2);


// type conversion: converting one datype to another datatype is called type conversion
let p4=2
let p5=String(p4)
console.log(p5, typeof p5);

let a3='40'
console.log(a3, typeof a3);
let a4=Number(a3)
console.log(a4, typeof a4);

let a5=Boolean(a3)
console.log(a5, typeof a5);

console.log(40+10+Number('40')+Number(true)+Number(false));










            
            

