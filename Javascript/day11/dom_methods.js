// dom methods
// method is a predefined function 
// 1.  indirect access methods 
// 2. direct access methods
    // i) document.body         -it gets the elements 
            let body=document.body
            console.log(body)
    // ii) document.head
            let head=document.head
            console.log(head)
    // iii) document.links
            let links=document.links
            console.log(links)      
            console.log(links[0]);
    // iv) document.images
            let images=document.images
            console.log(images);
            console.log(images[1]);
    // v) document.forms
            let forms=document.forms
            console.log(forms);
    // vi) document.url
            let urls=document.URL
            console.log(urls);
    // vii)document.baseuri
            let base=document.baseURI
            console.log(base);

// indirect access methods

    // 1) document.getElementById('idname')
    let heading1=document.getElementById("h1")
    console.log(heading1);

    // 2) document.getElementByClassName('classname')
    let clas1=document.getElementsByClassName("links")
    console.log(clas1);
    console.log(clas1[2]);

    // 3 document.getElementByTagName('tagname')
    let tag=document.getElementsByTagName('a')
    console.log(tag);

    // 4 document.queryselector("idname or classname or tagname")
    let h2=document.querySelector('#h1')
    console.log(h2);

    // 5 document.queryselectorall("idname or classname or tagname")
    let h3=document.querySelector('.links')
    console.log(h3);

    // 6 document.getElementsByName("name")         here name  is attribute of input tag in html
    let h4=document.getElementsByName('inp')
    console.log(h4);

// dom traversals

        // 1. first child()
        let fc=document.body.firstChild
        console.log(fc);
            // 1.2. first element child()
            let fec=document.body.firstElementChild
            console.log(fec);


        // 2. last child()
        let lc=document.body.lastChild
        console.log(lc);
            // 2.1 last element child()
            let lec=document.body.lastElementChild
            console.log(lec);


        // 3. parent ()
        let pn=document.querySelector('#h1')
        console.log(pn.parent);
            // 3.1 parent element()
            let pe=document.querySelector('#h1')
            console.log(pe.parentElement);


        // 4. next sibling()
        let ns=document.body.firstElementChild
        console.log(ns.nextSibling);

            // 4.1 next element sibling()
            let nes=document.body.firstElementChild
            console.log(nes.nextElementSibling);
            // 4.2 next next element sibling()
            let nn=document.body.firstElementChild
            console.log(nn.nextElementSibling.nextElementSibling);


        // 5. previous sibling()
        let ps=document.body.lastElementChild
        console.log(ps.previousSibling);

            // 5.1 previous element sibling()
            let pes=document.body.lastElementChild
            console.log(pes.previousElementSibling);

            // 5.2 previous previous element sibling()
            let ppes=document.body.lastElementChild
            console.log(ppes.previousElementSibling.previousElementSibling);

        // 6. child nodes()
        let cn=document.body
        console.log(cn.childNodes);
                // 6.1. child element nodes()
                let cen=document.body
                console.log(cen.children);


        // 7. children()
        let ch=document.body
        console.log(ch.children);
                
        

        // 8. previous element sibling()
        let pesib=document.body.lastElementChild
        console.log(pesib.previousElementSibling);
                // 8.1 previous previous element sibling()
                let ppesib=document.body.lastElementChild
                console.log(ppesib.previousElementSibling.previousElementSibling);

        // 9.previous parent()
        let pp=document.querySelector('#h1')
        console.log(pp.parentNode);
                // 9.1 previous parent element()
                let ppe=document.querySelector('#h1')
                console.log(ppe.parentElement);
    
        