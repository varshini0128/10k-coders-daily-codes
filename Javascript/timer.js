let hrs=0
let minutes=0
let seconds=0
let interval;

display.textContent="00:00:00"

function updatedisplay(){

        hrs=hrs<10 ? "0"+hrs:hrs
        minutes=minutes<10? "0"+minutes:minutes
        seconds=seconds<10? "0"+seconds: seconds

        display.textContent=`${hrs}:${minutes}:${seconds}`
}

start. addEventListener("click", ()=>{
    setInterval(()=>{
        seconds++
        if(seconds==60){
            seconds=0
            minutes++
        }
        if(minutes==60){
            minutes=0
            hrs++
        }
    },1000
    )

})