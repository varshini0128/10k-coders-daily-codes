// Strings
// string is a collection of characters enclosed in single quotes, double quotes or backticks.
// ways of defining a string
// 1. using string literals
// i.using single quotations
let str1='hello world'
console.log(typeof str1);
// ii. using double quotations
let str2="who's there?"
console.log(typeof str2);
// iii. using backticks
let str3=`welcome to js
programming
language`
console.log(typeof str3);

// 2. using string constructor
let str4=String('hello')
console.log(str4);

// using new keyword
let str5= new String('world')
console.log(str5,typeof str5);  // [String: 'world'] 'object'
// when we create a string using new keyword it creates a string object and the type of that is object  


// accessing the string values 
let s1='js is a programming language'
console.log(s1);
console.log(s1[1]);
// console.log(s1[-1]);undefined //we cant access negative index values in string

// methods of string
// methods are predefined functions in js
// 1. length
console.log(s1.length);

// 2. indexOf()
console.log(s1.indexOf('a')); 

// 3. lastIndexOf()
console.log(s1.lastIndexOf('l'));


// 4. concat()
let s2 ='and it is used for web development, '
let s3='widely used for frontend development'
console.log(s1.concat(s2,s3));

// 5. tolowercase()
let k='KITE'
console.log(k.toLowerCase());

//6. toUpperCase()
console.log(s1.toUpperCase());

//7. trim()
let s4='             hello world k                '
console.log(s4.trim());
console.log(s4.trim().length);

//8. trimStart()
console.log(s4.trimStart());
console.log(s4.trimStart().length);  

//9. trimEnd()
console.log(s4.trimEnd());
console.log(s4.trimEnd().length);

//10. split()
let s5='widely used for frontend development'
let splited=s5.split(" ")
console.log(splited);
let split1=s5.split(" ",3)
console.log(split1);


//11. at() returns char at given index
console.log(s5.at(3));
console.log(s5.at(-4));

//12. slice()
let sliced2=s5.slice(6,14)
console.log(sliced2);
let sliced=s5.slice(-6,-2)
console.log(sliced);


//13. substring(start)
console.log(s5.substring(0,6));

console.log(s5.substring(-5)); //it converts neg index to zero and print entire string

console.log(s5.substring(0,-6)); //empty line 

//14.replace()
let s6 = 'kkkkkkkkkk   hello python    kkkkkkkkkkk'
console.log(s6.replace('python','javascript'));

//15. replaceAll(old,new)
console.log(s6.replaceAll('k','*'));

//16. startsWith()
console.log(s6.startsWith('k'));

console.log(s6.startsWith('l'));


//17. endsWith(searchstring,position)
kk='hello world'
console.log(kk.endsWith('k'));

console.log(kk.endsWith('e',2));

//18. repeat()
console.log(s1.repeat(10))











