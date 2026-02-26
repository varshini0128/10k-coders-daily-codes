// simple calculator +-/%*
body=document.body
add1=document.getElementById('add')
inp1=document.getElementsByid(inp1)
function display(values){
    inp1.value+=values
}
function calculate(){
    inp1.value=eval(inp1.value)
}
function Allclear(){
    inp1.value=''
}
function delete1(){
    inp1.value=inp1.value.substr(0,inp1.value.length-1)

}

