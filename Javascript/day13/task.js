let body=document.body
let nav=document.createElement('navbar')
body.appendChild(nav)
nav.classList.add('navbar')

let ul=document.createElement("ul")
ul.classList.add('ul')
nav.appendChild(ul)
let li=document.createElement("li")
li.textContent="VARSH"
ul.appendChild(li)

let li1=document.createElement("li")
li1.textContent="HOME"
ul.appendChild(li1)

let li2=document.createElement("li")
li2.textContent="ABOUT"
ul.appendChild(li2)

let li3=document.createElement("li")
li3.textContent="LOGIN"
ul.appendChild(li3)


let section1=document.createElement("section")
body.appendChild(section1)
section1.classList.add('section1')

let img=document.createElement("img")
img.src="https://www.w3schools.com/w3images/girl.jpg"
img.style.height="400px"
section1.appendChild(img)
section1.style.marginLeft='80px'
let img1=document.createElement("img")
img1.src="https://www.w3schools.com/w3images/girl_train.jpg"
img1.style.height="400px"
section1.appendChild(img1)
let img2=document.createElement("img")
img2.src="https://www.w3schools.com/w3images/man_bench.jpg"
img2.style.height="400px"
section1.appendChild(img2)
let img3=document.createElement("img")
img3.src="https://www.w3schools.com/w3images/natureboy.jpg"
img3.style.height="400px"
section1.appendChild(img3)



let section2=document.createElement("section")
body.appendChild(section2)
section2.classList.add('section2')



let img4=document.createElement("img")
img4.src="https://www.w3schools.com/w3images/boy.jpg"
img4.style.height="400px"
section2.appendChild(img4)
section2.style.marginLeft='80px'
let img5=document.createElement("img")
img5.src="https://www.w3schools.com/w3images/man_bench.jpg"
img5.style.height="400px"
section2.appendChild(img5)
let img6=document.createElement("img")
img6.src="https://www.w3schools.com/w3images/girl_mountain.jpg"
img6.style.height="400px"
section2.appendChild(img6)
let img7=document.createElement("img")
img7.src="https://www.w3schools.com/w3images/girl_train.jpg"
img7.style.height="400px"
section2.appendChild(img7)


let section3=document.createElement("section")
body.appendChild(section3)
section3.classList.add('section3')



let img8=document.createElement("img")
img8.src="https://www.w3schools.com/w3images/boy.jpg"
img8.style.height="400px"
section3.appendChild(img8)
section3.style.marginLeft='80px'
let img9=document.createElement("img")
img9.src="https://www.w3schools.com/w3images/man_bench.jpg"
img9.style.height="400px"
section3.appendChild(img9)
let img10=document.createElement("img")
img10.src="https://www.w3schools.com/w3images/closegirl.jpg"
img10.style.height="400px"
section3.appendChild(img10)
let img11=document.createElement("img")
img11.src="https://www.w3schools.com/w3images/girl.jpg"
img11.style.height="400px"
section3.appendChild(img11)



var section = document.createElement('div');
var title = document.createElement('h1');
var image = document.createElement('img');

title.innerHTML = "About Me";
image.src = "https://www.w3schools.com/w3images/avatar_hat.jpg"; 

section.style.backgroundColor = "#555555";
section.style.textAlign = "center";
section.style.padding = "50px";
section.style.color = "white";
section.style.fontFamily = "Arial";

image.style.width = "100%";
image.style.maxWidth = "600px";

section.appendChild(title);
section.appendChild(image);
document.body.appendChild(section);


var nameHeader = document.createElement('h2');
nameHeader.innerHTML = "My Name";
nameHeader.style.textAlign = "justify";
nameHeader.style.marginTop = "40px";
nameHeader.style.paddingLeft='350px'
var bio = document.createElement('p');
bio.innerHTML = "Some text about me. I love taking photos of PEOPLE. I am lorem ipsum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.";
bio.style.textAlign = "justify";
bio.style.lineHeight = "1.6";
bio.style.paddingLeft='350px'
bio.style.paddingRight='350px'

var contactMail = document.createElement('p');
contactMail.innerHTML = "mail: example@example.com";
contactMail.style.textAlign = "justify";
contactMail.style.paddingLeft='350px'
var contactTel = document.createElement('p');
contactTel.innerHTML = "tel: 5353 35531";
contactTel.style.textAlign = "justify";
contactTel.style.paddingLeft='350px'

var divider = document.createElement('hr');
divider.style.border = "0.5px solid #777";
divider.style.margin = "30px 0";


var skillsHeader = document.createElement('h3');
skillsHeader.innerHTML = "Technical Skills";
skillsHeader.style.textAlign = "center";
skillsHeader.style.letterSpacing = "2px";
skillsHeader.style.paddingLeft='350px'
skillsHeader.style.paddingRight='350px'
function createSkillBar(skillName, percentage) {
    var label = document.createElement('p');
    label.innerHTML = skillName;
    label.style.textAlign = "center";
    label.style.letterSpacing = "4px";
    label.style.marginBottom = "10px";

    var greyBackground = document.createElement('div');
    greyBackground.style.backgroundColor = "white";
    greyBackground.style.height = "30px";
    greyBackground.style.marginBottom = "20px";

    var progressFill = document.createElement('div');
    progressFill.style.backgroundColor = "#999";
    progressFill.style.height = "100%";
    progressFill.style.width = percentage; // Use the percentage passed to the function
    progressFill.style.textAlign = "center";
    progressFill.style.lineHeight = "30px";
    progressFill.style.color = "black";
    progressFill.innerHTML = percentage;

    greyBackground.appendChild(progressFill);
    section.appendChild(label);
    section.appendChild(greyBackground);
}

section.appendChild(nameHeader);
section.appendChild(bio);
section.appendChild(contactMail);
section.appendChild(contactTel);
section.appendChild(divider);
section.appendChild(skillsHeader);


createSkillBar("Photography", "95%");
createSkillBar("Web Design", "85%");
createSkillBar("Photoshop", "80%");




var pricingTitle = document.createElement('h2');
pricingTitle.innerHTML = "How much I charge";
pricingTitle.style.textAlign = "left";
pricingTitle.style.marginTop = "50px";
pricingTitle.style.marginBottom = "30px";
pricingTitle.style.marginLeft = "580px";

section.appendChild(pricingTitle);


var tableContainer = document.createElement('div');
tableContainer.style.display = "flex";
tableContainer.style.gap = "20px";
tableContainer.style.justifyContent = "center";
section.appendChild(tableContainer);


function createPriceTable(title, price, features, isDark) {
    var table = document.createElement('div');
    table.style.width = "300px";
    table.style.backgroundColor = isDark ? "#c1c1c1" : "white"; // Grey for Pro, White for Basic
    table.style.color = "black";
    table.style.textAlign = "center";

    var header = document.createElement('div');
    header.innerHTML = title;
    header.style.padding = "30px";
    header.style.fontSize = "24px";
    header.style.backgroundColor = isDark ? "#333" : "black";
    header.style.color = "white";
    table.appendChild(header);

  
    for (var i = 0; i < features.length; i++) {
        var feature = document.createElement('div');
        feature.innerHTML = features[i];
        feature.style.padding = "15px";
        feature.style.borderBottom = "1px solid #ddd";
        table.appendChild(feature);
    }


    var priceArea = document.createElement('div');
    priceArea.style.padding = "30px";
    priceArea.innerHTML = "<h2 style='margin:0'>$ " + price + "</h2><p style='color:#777'>per month</p>";
    table.appendChild(priceArea);


    var footer = document.createElement('div');
    footer.style.padding = "20px";
    footer.style.backgroundColor = isDark ? "#b1b1b1" : "#f1f1f1";
    
    var btn = document.createElement('button');
    btn.innerHTML = "Sign Up";
    btn.style.padding = "10px 20px";
    btn.style.border = "none";
    btn.style.cursor = "pointer";
    btn.style.backgroundColor = isDark ? "#999" : "white";
    
    footer.appendChild(btn);
    table.appendChild(footer);

    tableContainer.appendChild(table);
}


createPriceTable("Basic", "10", ["Web Design", "Photography", "5GB Storage", "Mail Support"], false);
createPriceTable("Pro", "25", ["Web Design", "Photography", "50GB Storage", "Endless Support"], true);




var contactSection = document.createElement('div');
contactSection.style.backgroundColor = "#f1f1f1";
contactSection.style.color = "black";
contactSection.style.padding = "60px 20px";
contactSection.style.fontFamily = "sans-serif";
document.body.appendChild(contactSection);

var contactTitle = document.createElement('h2');
contactTitle.innerHTML = "Contact Me";
contactTitle.style.textAlign = "center";
contactSection.appendChild(contactTitle);

var contactIntro = document.createElement('p');
contactIntro.innerHTML = "Do you want me to photograph you? Fill out the form and fill me in with the details :) I love meeting new people!";
contactIntro.style.textAlign = "center";
contactIntro.style.maxWidth = "600px";
contactIntro.style.margin = "0 auto 30px auto";
contactSection.appendChild(contactIntro);

var formWrapper = document.createElement('div');
formWrapper.style.maxWidth = "600px";
formWrapper.style.margin = "0 auto";
contactSection.appendChild(formWrapper);

function createInputField(labelText) {
    var label = document.createElement('p');
    label.innerHTML = labelText;
    label.style.marginBottom = "5px";
    
    var input = document.createElement('input');
    input.style.width = "100%";
    input.style.padding = "12px";
    input.style.border = "1px solid #ccc";
    input.style.marginBottom = "20px";
    input.style.boxSizing = "border-box"; // Ensures padding doesn't break the width
    
    formWrapper.appendChild(label);
    formWrapper.appendChild(input);
}

createInputField("Name");
createInputField("Email");
createInputField("Message");

var sendBtn = document.createElement('button');
sendBtn.innerHTML = "Send Message";
sendBtn.style.width = "100%";
sendBtn.style.padding = "15px";
sendBtn.style.backgroundColor = "black";
sendBtn.style.color = "white";
sendBtn.style.border = "none";
sendBtn.style.cursor = "pointer";
sendBtn.style.fontSize = "16px";

sendBtn.onclick = function() {
    alert("Message Sent!");
};

formWrapper.appendChild(sendBtn);


var footer = document.createElement('footer');
footer.style.backgroundColor = "#9e9e9e"; // Light grey background
footer.style.color = "black";
footer.style.padding = "40px 20px";
footer.style.display = "flex";
footer.style.justifyContent = "space-around";
footer.style.fontFamily = "sans-serif";
document.body.appendChild(footer);

var infoCol = document.createElement('div');
infoCol.style.width = "30%";
var infoTitle = document.createElement('h3');
infoTitle.innerHTML = "INFO";
var infoText = document.createElement('p');
infoText.innerHTML = "Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.";
infoCol.appendChild(infoTitle);
infoCol.appendChild(infoText);
footer.appendChild(infoCol);

var blogCol = document.createElement('div');
blogCol.style.width = "30%";
var blogTitle = document.createElement('h3');
blogTitle.innerHTML = "BLOG POSTS";
blogCol.appendChild(blogTitle);

function addBlogEntry(imgSrc, title, desc) {
    var entry = document.createElement('div');
    entry.style.display = "flex";
    entry.style.alignItems = "center";
    entry.style.marginBottom = "10px";
    entry.style.borderBottom = "1px solid #888";
    entry.style.paddingBottom = "10px";

    var img = document.createElement('img');
    img.src = imgSrc;
    img.style.width = "50px";
    img.style.marginRight = "10px";

    var textPart = document.createElement('div');
    textPart.innerHTML = "<b>" + title + "</b><br>" + desc;

    entry.appendChild(img);
    entry.appendChild(textPart);
    blogCol.appendChild(entry);
}

addBlogEntry("https://via.placeholder.com/50", "Lorem", "Sed mattis nunc");
addBlogEntry("https://via.placeholder.com/50", "Ipsum", "Praes tinci sed");
footer.appendChild(blogCol);

var tagsCol = document.createElement('div');
tagsCol.style.width = "30%";
var tagsTitle = document.createElement('h3');
tagsTitle.innerHTML = "POPULAR TAGS";
tagsCol.appendChild(tagsTitle);

var tagsList = ["Travel", "New York", "London", "IKEA", "NORWAY", "DIY", "Ideas", "Baby", "Family"];
tagsList.forEach(function(tagName) {
    var tag = document.createElement('span');
    tag.innerHTML = tagName;
    tag.style.display = "inline-block";
    tag.style.padding = "5px 10px";
    tag.style.margin = "2px";
    tag.style.fontSize = "12px";
    tag.style.backgroundColor = (tagName === "Travel") ? "black" : "#616161";
    tag.style.color = "white";
    tagsCol.appendChild(tag);
});
footer.appendChild(tagsCol);

var bottomBar = document.createElement('div');
bottomBar.style.backgroundColor = "black";
bottomBar.style.color = "white";
bottomBar.style.textAlign = "center";
bottomBar.style.padding = "20px";
bottomBar.innerHTML = 'Powered by <a href="#" style="color:white">w3.css</a>';
document.body.appendChild(bottomBar);


