// nested function
//                writing the function inside a nested function is known as nested functions
// syntax: function demo(){
//                      function d1(){
//                      statements
//                       }
//                     }
function demo(){
    console.log("this is demo function");
    function d1(){
        console.log("this is d1 function");
        function d11(){
            console.log("this is d11 function");
        }
        function d12(){
            console.log("this is d22 function");
        }
        return [d11,d12]
    }
    
    function d2(){
        console.log("this is d2 function");
        
    }
    return [d1,d2]
}
demo()[0]()
demo()[1]()
demo()[0]()[0]()
demo()[0]()[1]()

let a = "global"
function demo1(){
    console.log(a);
    function inner(){
        console.log(a); 
    }
    return inner
}
demo1()()

function outer(){
    console.log("outer");
    let c=8
    function inner(){
        let b=9
        console.log(c);
    }
    // console.log(b);
    return inner
}
outer()()
// console.log(c)
// console.log(b)

// closure: it remembers the 

