let form1 = document.getElementById("form1")
let table = document.getElementById("table")
let inp1 = document.getElementById("inp1")
let inp2 = document.getElementById("inp2")
let inp3 = document.getElementById("inp3")

form1.addEventListener("click", (e) => {
    e.preventDefault()

    if (e.target.textContent === 'Add') {

        if (inp1.value !== "" && inp2.value !== "" && inp3.value !== "") {

            table.innerHTML += `
            <tr>
                <td>${inp1.value}</td>
                <td>${inp2.value}</td>
                <td>${inp3.value}</td>
                <td><button>Edit</button></td>
                <td><button>Delete</button></td>
            </tr>
            `

            inp1.value = ""
            inp2.value = ""
            inp3.value = ""
        }
    }

    else if (e.target.textContent === 'Edit') {

        let row = e.target.parentElement.parentElement
        let cells = row.children

        inp1.value = cells[0].textContent
        inp2.value = cells[1].textContent
        inp3.value = cells[2].textContent

        e.target.textContent = 'Update'
    }

    else if (e.target.textContent === 'Update') {

        let row = e.target.parentElement.parentElement
        let cells = row.children

        cells[0].textContent = inp1.value
        cells[1].textContent = inp2.value
        cells[2].textContent = inp3.value

        e.target.textContent = 'Edit'

        inp1.value = ""
        inp2.value = ""
        inp3.value = ""
    }

    else if (e.target.textContent === 'Delete') {

        e.target.parentElement.parentElement.remove()
    }
})
