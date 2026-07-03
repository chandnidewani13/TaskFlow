const typingStatus =

document.getElementById(

'typingStatus'
);


document.getElementById(

'chatMessage'

).addEventListener(

'input',

() => {

typingStatus.innerHTML =

"Someone is typing...";
});


setInterval(() => {

typingStatus.innerHTML = "";

}, 2000);