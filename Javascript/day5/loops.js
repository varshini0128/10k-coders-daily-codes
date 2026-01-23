// loops: to execute multiples lines of statements in a single statement
// loops are used to reduce the code length
// types of loops:
        // 1) for loop: when we know the no of iterations then we use for loop
        // syntax : for (variable declaration ; condition; increment/decrement;){
                        // statements
                      // }
        for(let i=1;i<10;i++){
            console.log(i);
        }
for (let i=1;i<=10;i++){
    console.log('hello world');
}
// while loop: when we dont know the no of iterations
// syntax: while (condition){
            // stmnts
            // }

let a = 1
while (a<=10){
    console.log(a);
    a++
}

// do-while
// if the condition is true or false 
do{
    console.log(a);
    a++
}while (a<=10);

// print even from 1 to 50
for (let a=1; a<=50; a++){
    if (a%2==0){
        console.log(a);
    }
}
for (let a=1; a<=50; a++){
    if (a%2!=0){
        console.log(a);
    }
}
// reverse a string
let s ="hello"
rev=''
for (let i=0;i<=s.length-1;i++){
    rev=s[i]+rev
}
console.log(rev);


// print the sum of 50 numbers by using while loop
// sum=0
// for (let a=1; a<=50; a++){
//    sum+=a
// }
// console.log(sum);
p=1
s1=0
while (p<=50){
    s1+=p
    p++
}
console.log(s1);


// sum of even numbers using while loop
s=1
even_sum=0
while (s<=50){
    if (s%2==0){
        even_sum+=s
    }
    s++
}
console.log(even_sum);

// sum of odd numbers using while loop
s2=1
odd_sum=0
while (s2<=50){
    if (s2%2!=0){
        odd_sum+=s2
    }
    s2++
}
console.log(odd_sum);


// print table of given number
k=5
for (let r=1; r<=10;r++){
    // console.log(k +' '+'x',r,'=',k*r);
    console.log(`${k}x${r}=${k*r}`);
    
}

// print multiples of 5 from 1to 100

for (let i=1;i<=100;i++){
   if(i%5==0){
    console.log(i);
   }
}
// factorial
p=3
fact=1
for (let i=1;i<=p;i++){
    fact*=i
}
console.log(fact);


// reverse a number
let num=123
rev=0
while(num>0){
    rem=num%10;
    rev=rev*10+rem;
    num=Math.floor(num/10);
}
console.log(rev);
