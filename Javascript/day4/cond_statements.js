// conditional statements:
// it is used to check the condition and print the suitable inner statements

// use cases: login 
            // authentication 
            // age eligibilty criteria

// types of conditional statements
// 1)if condition: it returns the value when the condition is true
// 2)else if : when we want to check the multiple conditions
// 3)else: when if and else-if doesnt satisfy else executes
let a= 30
if (a>34){
    console.log("a is greater than 34");
}
else if (a==30){
    console.log( "a is equal to 30");
}else{
    console.log("zero");
}
// 4)nested if :
// when we want to satisfy the all conditions

// check if the number is divisible by 3 or 5
let p=15
if(a%3==0){
    if(a%5==0){
        console.log("divisible by both");
    }
    else{
        console.log("divisible by 3");
        
    }
}
else{
    console.log("not divisible by both 3 and 5");
}

// switch case()

let day=1
switch (day){
    case 1:
        console.log("sunday");
        break
    case 2:
         console.log("monday");
         break
    case 3:
        console.log("tuesday");
        break
    case 4:
        console.log("wednesday");
        break
    case 5:
        console.log("thursday");
        break
    case 6:
        console.log("friday");
        break
    case 7:
        console.log("satday");
        break
    default:
        console.log("check your input");
        break
}
// if given number is even or odd
let k = 60;
if (k%2==0){
    console.log("even");
}
else{
    console.log("odd");
}

// driving license and vote
age=20
if (age>18){
        console.log("eligible");
}
else{
    console.log("not eligible"); 
}
 
// divisible by 2,3 and 6
if (a%2==0){
    if(a%3==0){
        if(a%6==0){
            console.log("divisible by 2 , 3 and 6");
            
        }
        else{
            console.log("divisible by 2and3");
        }
    }
}
else{
    console.log("not divisble by 2,3,6");
}
// check the biggest value among three numbers
k1=8
k2=9
k3=10
if (k1>k2 && k1>k3){
    console.log("k1 is greater");
}
else if (k2>k1 && k2>k3){
    console.log("k2 is greater");
}
else if (k3>k2 && k3>k1){
    console.log("k3 is greater");
}


// leap year
let year = 2024;

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)){
    
        console.log(`${year}, is a leap year: isLeapYear`);
}
else{
    console.log("not a leap year");
    
}


char = 'B'; 
ascii = char.charCodeAt(0);

if (ascii % 2 === 0) {
    
    powerOfTwo = 2 ** ascii;
    console.log(char + " has an even ASCII (" + ascii + "). 2^" + ascii + " is: " + powerOfTwo);
} else {
    console.log(char + " has an odd ASCII (" + ascii + ").");
}
