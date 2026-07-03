import {

initializeApp

}

from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";


import {

getAuth,

createUserWithEmailAndPassword,

signInWithEmailAndPassword,

sendEmailVerification,

sendPasswordResetEmail,

signOut

}

from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";



/* =========================================
   FIREBASE CONFIG
========================================= */

const firebaseConfig = {

apiKey:
"AIzaSyCGAC8n3GRe4AX_As_BSCJb8wLpg62IH6s",

authDomain:
"fomca0006-internship.firebaseapp.com",

projectId:
"fomca0006-internship",

storageBucket:
"fomca0006-internship.firebasestorage.app",

messagingSenderId:
"565201524954",

appId:
"1:565201524954:web:8c5ef31b28ae1b781e6de3"
};


/* =========================================
   INITIALIZE FIREBASE
========================================= */

const app = initializeApp(firebaseConfig);

const auth = getAuth(app);



/* =========================================
   REGISTER USER
========================================= */

window.registerUser = async function () {

const email =

document.getElementById(
'email'
).value;


const password =

document.getElementById(
'password'
).value;


const role =

document.getElementById(
'role'
).value;


try {

const userCredential =

await createUserWithEmailAndPassword(

auth,
email,
password
);


await sendEmailVerification(

userCredential.user
);


alert(

"Registration successful! Verification email sent."
);


/* SAVE ROLE */

localStorage.setItem(

"userRole",
role
);


window.location.href = "/";

}

catch(error) {

alert(error.message);

}
};



/* =========================================
   LOGIN USER
========================================= */

window.loginUser = async function () {

const email =

document.getElementById(
'email'
).value;


const password =

document.getElementById(
'password'
).value;


try {

const userCredential =

await signInWithEmailAndPassword(

auth,
email,
password
);


const user = userCredential.user;


/* VERIFY EMAIL */

if (!user.emailVerified) {

alert(

"Please verify your email first."
);

return;
}


/* GET ROLE */

const role = localStorage.getItem(

"userRole"
);


/* ROLE REDIRECTS */

if (role === "admin") {

window.location.href =
"/admin-dashboard/";
}


else if (role === "business") {

window.location.href =
"/business-dashboard/";
}


else if (role === "leader") {

    alert("FIREBASE-AUTH.JS LEADER REDIRECT");

    window.location.href = "/leader/dashboard/";
}

else {

window.location.href =
"/employee-dashboard/";
}

}

catch(error) {

alert(error.message);

}
};



/* =========================================
   RESET PASSWORD
========================================= */

window.resetPassword = async function () {

const email = document.getElementById(
'resetEmail'
).value.trim();

if(email === "") {

alert("Please enter email");

return;
}

try {

await sendPasswordResetEmail(
auth,
email
);

alert(
"Reset password email sent successfully! Check Inbox or Spam."
);

console.log(
"RESET EMAIL SENT"
);

}
catch(error) {

console.log(error);

alert(
error.message
);

}
};


/* =========================================
   LOGOUT USER
========================================= */

window.logoutUser = async function () {

try {

await signOut(auth);

alert(

"Logged out successfully"
);

window.location.href = "/";

}

catch(error) {

alert(error.message);

}
};