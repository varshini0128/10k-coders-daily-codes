// objects:
//      objects is a real world entity, it is used to store values in the form of key and value pairs
//      it is defined by using  {}
// ways of creating a objects
// ----------------------------
// 1.by using object literals
let laptop={
    'brand':'hp',
    'color':'silver',
    'cost':'400000'

}
console.log(laptop);



// 2. by using object constructor
// let obj1=object()
// console.log(obj1);


// // 3. by using new keyword
// let obj2=new object()
// console.log(obj2);

// 4. by using function constructor
function obj3(name,color){
    this.name=name
    this.color=color
    console.log(this.name);
    console.log(this.color);
}

let obj9=obj3('dell','grey')
let obj0=obj3('hp','black')


// let obj5=new Obj3('new lappy','black')
// console.log(obj5);


// accesing values from the objects
// 1)  . dot notation
// 2)   bracket notation
let mobile={
    name:'vivo',
    model:'z1 pro',
    color:'black',
    cost:20000
}
console.log(mobile);
console.log(mobile.color);
console.log(mobile.model);
console.log(mobile.cost);
console.log(mobile.name);

// 2)   bracket notation
let mobile1={
    'name of mobile':'samsung',
    model:'A51',
    color:'black',
    cost:50000
}
console.log(mobile1["name of mobile"]); //spaces kosam
console.log(mobile1["cost"]);

mobile1.storage=200
console.log(mobile1);
mobile1['height']=150
console.log(mobile1);

delete mobile1.model
console.log(mobile1);

// object methods:
// keys()
console.log(Object.keys(mobile1));
// values()
console.log(Object.values(mobile1));
// assign()
let mobile2={
    name:'oneplus',
    model:'nord',
    color:'blue',
    cost:30000
}
let mobile3=Object.assign({},mobile2)
console.log(mobile3);
// entries()
console.log(Object.entries(mobile1));
// seal()
Object.seal(mobile1)
mobile1.ram=8
console.log(mobile1,"******");
mobile1.color='blue'
console.log(mobile1);
// freeze()
Object.freeze(mobile1)
mobile1.ram=16
console.log(mobile1);
mobile1.color='red'
console.log(mobile1);

