// array: array is a collection of homogenous and heterogenous elements in it 
// collection data type
// array created using [ ] array literals 

// array can be created in three ways 
// 1. by using array literals 
// --------------------------
let arr=[3,24,'ram',30.3,true,(1,2,3),{a:1,b:4,c:5}]
console.log(arr);   //[3, 24, 'ram', 30.3, true, 3, {…}]


// 2. by using array constructor

let arr1=Array()

console.log(arr1);  //[]


// 3. by using new keyword

let arr2=new Array()
console.log(arr2);    //[]



// how to access the elements from array 
// -----------------------------------------
//[3,24,'ram',30.3,true,(1,2,3),{a:1,b:4,c:5}]
console.log(arr[3]);  //30.3

console.log(arr[-1],'******'); //we cant access negative index values in array
//  if did so then we get as undefined

// only positive index are available no negative index is allowed by js



// how to modify an array
let product=['tablet','mobile','speaker','keyboard']
product[0]='mango'
console.log(product);      //['mango', 'mobile', 'speaker', 'keyboard']
// it stores empty values as
//  (11) ['mango', 'mobile', 'speaker', 'keyboard', empty × 6, 'mango']
// 0:"mango"
// 1: "mobile"
// 2: "speaker"
// 3: "keyboard"
// 10: "mango"
product[10]='mango'
console.log(product);   //['mango', 'mobile', 'speaker', 'keyboard', empty × 6, 'mango']

delete product[0]
console.log(product,'----------------');
// after deleting the value in that position remains empty untill any other element is added in that position

// [empty, 'mobile', 'speaker', 'keyboard', empty × 6, 'mango']

// array constructor








// methods in arrays
// -------------------
// methods are predefined functions which are present in js

// 1.push():
// add elements at last and returns the new length of array 

let ar = [1,2,3,4]
ar.push(5)
console.log(ar);  // [1, 2, 3, 4, 5]
ar.push("students")  
console.log(ar); // [1, 2, 3, 4, 5, 'students']


ar.push(6,7,8,9,10)
console.log(ar);  // [1, 2, 3, 4, 5, 'students', 6, 7, 8, 9, 10]

// 2. pop()
// Removes the last element from an array and returns it.
//  If the array is empty, undefined is returned and the array is not modified.

ar.pop()
console.log(ar);   //[1, 2, 3, 4, 5, 'students', 6, 7, 8, 9]


// 3. unshift()
// Inserts new elements at the start of an array, and returns the new length of the array
ar.unshift(9)
console.log(ar);    //[9, 1, 2, 3, 4, 5, 'students', 6, 7, 8, 9]
ar.unshift(5,6,7,8)
console.log(ar);   //[5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 'students', 6, 7, 8, 9]



// 4. shift()
// Removes the first element from an array and returns it.
// If the array is empty, undefined is returned and the array is not modified.
ar.shift()
console.log(ar);    // [6, 7, 8, 9, 1, 2, 3, 4, 5, 'students', 6, 7, 8, 9]
// after removing next values takes its index position without leaving empty


// 5. concat()
// Combines two or more arrays. This method returns a new array without modifying any existing arrays.


let a1=[1,2]
let a2=[3,4]
let a3=[5,6]
let new_a=a1.concat(a2,a3)
console.log(new_a,'------------');   //[1, 2, 3, 4, 5, 6] '------------'
nw=a3.concat(a1,a2)
console.log(nw);    //  [5, 6, 1, 2, 3, 4]

// 6. indexOf:
// returns the index of the first occurrence of a value in an array,
// or -1 if it is not present.

let a=[1,2,3,2,3,2,4,5]
s=a.indexOf(2)
console.log(s);  //1
console.log(a.indexOf(2,4));   //5
console.log(a.indexOf(2,7));   //-1


// 7. includes(searchelement,fromindex)
// The element to search for.
// Determines whether an array includes a certain element, returning true or false as appropriate.


let a11=['a','b','c','d']
console.log(a11.includes('b'));  // true
console.log(a11.includes('b',2)); //false
console.log(a11.includes('v')); //false v is not in a11


// 8. at()
// Returns the item located at the specified index.
// The zero-based index of the desired code unit. A negative index will count back from the last item.
let b=[1,2,3,4,5,6,7,8,9]
console.log(b.at(5));
 


// 9. slice(start_index,end_index)
// Returns a copy of a section of an array. 
// For both start and end, a negative index can be used to indicate an offset from the end of the array.
// For example, -2 refers to the second to last element of the array.
let sliced=arr.slice(1)
console.log(sliced);
console.log(b.slice(3,7));


// 10. splice(start_index,delete_count,element1,element2,...)
// Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.
// Returns an array containing the deleted elements. If only one element is removed, an array of one element is returned. If no elements are removed, an empty array is returned.
let spliced=b.splice(3,4,10,11,12)
console.log(spliced);  //[4, 5, 6, 7]
console.log(b.splice(3,0,10,11,12));      //[] no element is removed


// 11. length
// The length property of an object which is an instance of type Array sets or returns the number of elements in that array.
console.log(b.length);

// 12. toString()
// The toString() method returns a string representing the specified array and its elements.
let c=[1,2,3,4,5]
console.log(c.toString());  //1,2,3,4,5

// 13. join()
// The join() method creates and returns a new string by concatenating all of the elements in an array (or an array-like object), 
// separated by commas or a specified separator string.
//  If the array has only one item, then that item will be returned without using the separator.
console.log(c.join());  //1,2,3,4,5
console.log(c.join(' '));  //1 2 3 4 5
console.log(c.join('-')); //1-2-3-4-5  
console.log(c.join('*')); //1*2*3*4*5


//  array itterating methods:
// 14a. forEach() method executes a provided function once for each array element.
let arr11=[1,2,3,4,5]
arr11.forEach((element,index)=>{
    console.log(element,index);
}) //  1 0
   //  2 1
   //  3 2
   //  4 3
   //  5 4


// 14b. map() method creates a new array populated with the results of calling a provided function on every element in the calling array.
let arr12=[1,2,3,4,5]   
let mapped=arr12.map((element,index)=>{
    return element*2
})
console.log(mapped);  //[2, 4, 6, 8, 10]


// 15 filter() method creates a new array with all elements that pass the test implemented by the provided function.
let arr13=[1,2,3,4,5,6,8,11,13,15,17]   
let filtered=arr13.filter((element,index)=>{
    return element%2==0
})
console.log(filtered);  //[2, 4, 6, 8]


// 16. reduce() method executes a reducer function (that you provide) on each element of the array, resulting in a single output value.
//syntax: array.reduce(function(total, currentValue, currentIndex, arr), initialValue)
let arr14=[1,2,3,4,5]
let reduced=arr14.reduce((accumulator,currentValue)=>{
    return accumulator+currentValue
})  
console.log(reduced);  //15


// 17. sort() method sorts the elements of an array in place and returns the sorted array. The default sort order is ascending, built upon converting the elements into strings, then comparing their sequences of UTF-16 code units values.
let arr15=[3,1,4,2,5,11,22,10,1,2]
arr15.sort((e,f)=>{
    return e-f
}   )
console.log(arr15); // [1, 1, 2, 2, 3, 4, 5, 10, 11, 22]
// f==>means second element and e==>means first element

let arr17=[3,1,4,2,5,11,22,10,1,2]
arr17.sort((e,f)=>{
    return f-e
}   )
console.log(arr17); // [1, 1, 2, 2, 3, 4, 5, 10, 11, 22]
console.log(arr17,'********');


// 18 find()
//  method returns the value of the first element in the provided array that satisfies the provided testing function. If no values satisfy the testing function, undefined is returned.
let arr18=[1,2,3,4,5,6,7,8,9]   
let found=arr18.find((element,index)=>{
    return element>5,'----'
})
console.log(found);  //6

// 19 findIndex() 
// method returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns -1, indicating that no element passed the test.
let arr19=[1,2,3,4,5,6,7,8,9]   
let foundIndex=arr19.findIndex((element,index)=>{
    return element>5
})
console.log(foundIndex);  //5


// 20 some() 
// method tests whether at least one element in the array passes the test implemented by the provided function. It returns a Boolean value.
let arr20=[1,2,3,4,5,6,7,8,9]
let some=arr20.some((element,index)=>{
    return element>5
})
console.log(some);  //true



// 21 every() method tests whether all elements in the array pass the test implemented by the provided function. It returns a Boolean value.
let arr21=[1,2,3,4,5,6,7,8,9]   
let every=arr21.every((element,index)=>{
    return element>5
})
console.log(every);  //false


// 22 reverse() method reverses an array in place. The first array element becomes the last, and the last array element becomes the first.
let arr22=[1,2,3,4,5]
arr22.reverse()
console.log(arr22);  //[5, 4, 3, 2, 1]