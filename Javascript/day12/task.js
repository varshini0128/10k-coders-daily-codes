let body = document.body;
body.style.margin = '0px';
body.style.fontFamily = 'Arial, sans-serif';

// navbar
body.innerHTML = `
<nav>
    <ul>
        <li>Home</li>
        <li>My Food</li>
        <li>Mail</li>
    </ul>
</nav>
`;

let nav = body.firstElementChild;
nav.style.borderBottom = '1px solid #ddd';
nav.style.position = 'sticky';
nav.style.top = '0';
nav.style.backgroundColor = 'white';

let ul = nav.firstElementChild;
ul.style.listStyle = 'none';
ul.style.display = 'flex';
ul.style.justifyContent = 'space-between';
ul.style.padding = '20px';
ul.style.margin = '0';
ul.style.fontSize = '20px';


let sec = document.createElement('section');
body.appendChild(sec);
sec.style.display = 'flex';
sec.style.justifyContent = 'space-evenly';
sec.style.padding = '40px 0px';

//  CARD 1 
let d1 = document.createElement('div');
sec.appendChild(d1);
d1.style.width = '280px';
d1.style.textAlign = 'center';

let i1 = document.createElement('img');
i1.src = "https://www.w3schools.com/w3images/sandwich.jpg";
i1.style.width = '100%';
i1.style.height = '350px';
d1.appendChild(i1);

let h1 = document.createElement('h3');
h1.innerText = 'The Perfect Sandwich, A Real NYC Classic';
d1.appendChild(h1);

let p1 = document.createElement('p');
p1.innerText = 'Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum.';
d1.appendChild(p1);

// CARD 2 
let d2 = document.createElement('div');
sec.appendChild(d2);
d2.style.width = '280px';
d2.style.textAlign = 'center';

let i2 = document.createElement('img');
i2.src = "https://www.w3schools.com/w3images/steak.jpg";
i2.style.width = '100%';
i2.style.height = '350px';
d2.appendChild(i2);

let h2 = document.createElement('h3');
h2.innerText = 'Let Me Tell You About This Steak';
d2.appendChild(h2);

let p2 = document.createElement('p');
p2.innerText = 'Once again, some random text to lorem lorem ipsum lorem ipsum text praesent tincidunt.';
d2.appendChild(p2);

// CARD 3
let d3 = document.createElement('div');
sec.appendChild(d3);
d3.style.width = '280px';
d3.style.textAlign = 'center';

let i3 = document.createElement('img');
i3.src = "https://www.w3schools.com/w3images/cherries.jpg";
i3.style.width = '100%';
i3.style.height = '350px';
d3.appendChild(i3);

let h3 = document.createElement('h3');
h3.innerText = 'Cherries, interrupted';
d3.appendChild(h3);

let p3 = document.createElement('p');
p3.innerText = 'Lorem ipsum text praesent tincidunt ipsum lipsum. What else?';
d3.appendChild(p3);

// CARD 4 
let d4 = document.createElement('div');
sec.appendChild(d4);
d4.style.width = '280px';
d4.style.textAlign = 'center';

let i4 = document.createElement('img');
i4.src = "https://www.w3schools.com/w3images/wine.jpg";
i4.style.width = '100%';
i4.style.height = '350px';
d4.appendChild(i4);

let h4 = document.createElement('h3');
h4.innerText = 'Once Again, Robust Wine and Vegetable Pasta';
d4.appendChild(h4);

let p4 = document.createElement('p');
p4.innerText = 'Lorem ipsum text praesent tincidunt ipsum lipsum.';
d4.appendChild(p4);


let sec2 = document.createElement('section');
body.appendChild(sec2);
sec2.style.display = 'flex';
sec2.style.justifyContent = 'space-evenly';
sec2.style.padding = '40px 0px';

//  CARD 5 
let d5 = document.createElement('div');
sec2.appendChild(d5);
d5.style.width = '280px';
d5.style.textAlign = 'center';

let i5 = document.createElement('img');
i5.src = "https://www.w3schools.com/w3images/popsicle.jpg"; 
i5.style.width = '100%';
i5.style.height = '350px';
// i5.style.backgroundSize = 'cover';
d5.appendChild(i5);

let h5 = document.createElement('h3');
h5.innerText = 'All I Need Is a Popsicle';
d5.appendChild(h5);

let p5 = document.createElement('p');
p5.innerText = 'Lorem ipsum text praesent tincidunt ipsum lipsum.';
d5.appendChild(p5);


//  CARD 6
let d6 = document.createElement('div');
sec2.appendChild(d6);
d6.style.width = '280px';
d6.style.textAlign = 'center';

let i6 = document.createElement('img');
i6.src = "https://www.w3schools.com/w3images/salmon.jpg"; 
i6.style.width = '100%';
i6.style.height = '350px';
// d6.style.backgroundSize = 'cover';
d6.appendChild(i6);

let h6 = document.createElement('h3');
h6.innerText = 'Salmon For Your Skin';
d6.appendChild(h6);

let p6 = document.createElement('p');
p6.innerText = 'Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum.';
d6.appendChild(p6);


// CARD 7 
let d7 = document.createElement('div');
sec2.appendChild(d7);
d7.style.width = '280px';
d7.style.textAlign = 'center';

let i7 = document.createElement('img');
i7.src = "https://www.w3schools.com/w3images/sandwich.jpg";
i7.style.width = '100%';
i7.style.height = '350px';
// i7.style.backgroundSize = 'cover';
d7.appendChild(i7);

let h7 = document.createElement('h3');
h7.innerText = 'The Perfect Sandwich, A Real Classic';
d7.appendChild(h7);

let p7 = document.createElement('p');
p7.innerText = 'Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum.';
d7.appendChild(p7);


// CARD 8 
let d8 = document.createElement('div');
sec2.appendChild(d8);
d8.style.width = '280px';
d8.style.textAlign = 'center';

let i8 = document.createElement('img');
i8.src = "https://www.w3schools.com/w3images/croissant.jpg"; 
i8.style.width = '100%';
i8.style.height = '350px';
// i8.style.backgroundSize = 'cover';
d8.appendChild(i8);

let h8 = document.createElement('h3');
h8.innerText = 'Le French';
d8.appendChild(h8);

let p8 = document.createElement('p');
p8.innerText = 'Lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum.';
d8.appendChild(p8);

let lb=document.createElement('hr')
body.appendChild(lb)
lb.style.marginLeft='250px'
lb.style.marginRight='250px'
sec2.innerHTML=`
            <br>
            `
let head=document.createElement('h1')
body.appendChild(head)
head.innerText='About Me, The Food Man'
head.style.textAlign='center'


let im=document.createElement('img')
body.appendChild(im)
im.src="https://www.w3schools.com/w3images/chef.jpg"
im.style.display='block'
im.style.marginLeft='350px'


let hw1=document.createElement('h2')
body.appendChild(hw1)
hw1.innerText='I am Who I Am!'
hw1.style.textAlign='center'

let p9 = document.createElement('p');
p9.innerText = 'With Passion For Real, Good Food';
body.appendChild(p9);
p9.style.textAlign='center'




let p10 = document.createElement('p');
p10.innerText = 'Just me, myself and I, exploring the universe of unknownment. I have a heart of love and an interest of lorem ipsum and mauris neque quam blog. I want to share my world with you. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla';
body.appendChild(p10);
p10.style.textAlign='center'
p10.style.marginLeft='230px'
p10.style.marginRight='190px'

// --- FOOTER SECTION ---
let foot = document.createElement('footer');
body.appendChild(foot);
foot.innerHTML=`
            <br>
            `
foot.style.display = 'flex';
foot.style.justifyContent = 'space-between';
foot.style.padding = '40px 10px';
foot.style.borderTop = '1px solid #ddd';
foot.style.marginTop = '40px';


let col1 = document.createElement('div');
foot.appendChild(col1);
col1.style.width = '30%';

let h1_f = document.createElement('h3');
h1_f.innerText = 'FOOTER';
col1.appendChild(h1_f);

let p1_f = document.createElement('p');
p1_f.innerText = 'Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.';
col1.appendChild(p1_f);

let pow = document.createElement('p');
pow.innerHTML = 'Powered by <a href="#">w3.css</a>';
col1.appendChild(pow);
col1.style.marginLeft='150px'


let col2 = document.createElement('div');
foot.appendChild(col2);
col2.style.width = '30%';

let h2_f = document.createElement('h3');
h2_f.innerText = 'BLOG POSTS';
col2.appendChild(h2_f);
col2.style.marginLeft='150px'

let post1 = document.createElement('div');
post1.style.display = 'flex';
post1.style.marginBottom = '10px';
col2.appendChild(post1);

let img_p1 = document.createElement('img');
img_p1.src = "https://www.w3schools.com/w3images/workshop.jpg";
img_p1.style.width = '50px';
img_p1.style.height = '50px';
img_p1.style.marginRight = '10px';
post1.appendChild(img_p1);

let text_p1 = document.createElement('span');
text_p1.innerHTML = '<b>Lorem</b><br>Sed mattis nunc';
post1.appendChild(text_p1);


let post2 = document.createElement('div');
post2.style.display = 'flex';
col2.appendChild(post2);

let img_p2 = document.createElement('img');
img_p2.src = "https://www.w3schools.com/w3images/gondol.jpg";
img_p2.style.width = '50px';
img_p2.style.height = '50px';
img_p2.style.marginRight = '10px';
post2.appendChild(img_p2);

let text_p2 = document.createElement('span');
text_p2.innerHTML = '<b>Ipsum</b><br>Praes tinci sed';
post2.appendChild(text_p2);


let col3 = document.createElement('div');
foot.appendChild(col3);
col3.style.width = '30%';

let h3_f = document.createElement('h3');
h3_f.innerText = 'POPULAR TAGS';
col3.appendChild(h3_f);

let tagContainer = document.createElement('div');
tagContainer.style.display = 'flex';
tagContainer.style.flexWrap = 'wrap';
tagContainer.style.gap = '5px';
tagContainer.style.marginRight='100px';
col3.appendChild(tagContainer);

let tag1 = document.createElement('span');
tag1.innerText = 'Travel';
tag1.style.backgroundColor = 'black';
tag1.style.color = 'white';
tag1.style.padding = '5px 10px';
tagContainer.appendChild(tag1);

let tag2 = document.createElement('span');
tag2.innerText = 'New York';
tag2.style.backgroundColor = '#616161';
tag2.style.color = 'white';
tag2.style.padding = '5px 10px';
tag2.style.fontSize = '12px';
tagContainer.appendChild(tag2);

let tag3 = document.createElement('span');
tag3.innerText = 'Dinner';
tag3.style.backgroundColor = '#616161';
tag3.style.color = 'white';
tag3.style.padding = '5px 10px';
tag3.style.fontSize = '12px';
tagContainer.appendChild(tag3);



let tag4 = document.createElement('span');
tag4.innerText = 'Salmon';
tag4.style.backgroundColor = '#616161';
tag4.style.color = 'white';
tag4.style.padding = '5px 10px';
tag4.style.fontSize = '12px';
tagContainer.appendChild(tag4);


let tag5 = document.createElement('span');
tag5.innerText = 'France';
tag5.style.backgroundColor = '#616161';
tag5.style.color = 'white';
tag5.style.padding = '5px 10px';
tag5.style.fontSize = '12px';
tagContainer.appendChild(tag5);

let tag6 = document.createElement('span');
tag6.innerText = 'Drinks';
tag6.style.backgroundColor = '#616161';
tag6.style.color = 'white';
tag6.style.padding = '5px 10px';
tag6.style.fontSize = '12px';
tagContainer.appendChild(tag6);


let tag7 = document.createElement('span');
tag7.innerText = 'Ideas';
tag7.style.backgroundColor = '#616161';
tag7.style.color = 'white';
tag7.style.padding = '5px 10px';
tag7.style.fontSize = '12px';
tagContainer.appendChild(tag7);



let tag8 = document.createElement('span');
tag8.innerText = 'Flavours';
tag8.style.backgroundColor = '#616161';
tag8.style.color = 'white';
tag8.style.padding = '5px 10px';
tag8.style.fontSize = '12px';
tagContainer.appendChild(tag8);



let tag9 = document.createElement('span');
tag9.innerText = 'Cuisine';
tag9.style.backgroundColor = '#616161';
tag9.style.color = 'white';
tag9.style.padding = '5px 10px';
tag9.style.fontSize = '12px';
tagContainer.appendChild(tag9);

let tag10 = document.createElement('span');
tag10.innerText = 'Chicken';
tag10.style.backgroundColor = '#616161';
tag10.style.color = 'white';
tag10.style.padding = '5px 10px';
tag10.style.fontSize = '12px';
tagContainer.appendChild(tag10);

let tag11 = document.createElement('span');
tag11.innerText = 'Dressing';
tag11.style.backgroundColor = '#616161';
tag11.style.color = 'white';
tag11.style.padding = '5px 10px';
tag11.style.fontSize = '12px';
tagContainer.appendChild(tag11);