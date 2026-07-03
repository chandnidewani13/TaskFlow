import { initializeApp }

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

import {

getFirestore,

collection,

addDoc,

getDocs,

query,

where

}

from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";


// FIREBASE CONFIG

const firebaseConfig = {

apiKey: "AIzaSyCGAC8n3GRe4AX_As_BSCJb8wLpg62IH6s",

authDomain: "fomca0006-internship.firebaseapp.com",

projectId: "fomca0006-internship",

storageBucket: "fomca0006-internship.firebasestorage.app",

messagingSenderId: "565201524954",

appId: "1:565201524954:web:8c5ef31b28ae1b781e6de3"
};


const app = initializeApp(firebaseConfig);

const auth = getAuth(app);

const db = getFirestore(app);


// REGISTER

window.registerUser = async function () {

const name =
document.getElementById('registerName').value;

const email =
document.getElementById('registerEmail').value;

const password =
document.getElementById('registerPassword').value;

const role =
document.getElementById('userRole').value;


try {

const userCredential =

await createUserWithEmailAndPassword(

auth,
email,
password
);

const user = userCredential.user;


// VERIFY EMAIL

await sendEmailVerification(user);


// SAVE USER

await addDoc(collection(db, "users"), {

name: name,

email: email,

role: role,

createdAt: new Date()
});


alert("Verification email sent!");

window.location.href = "/";

}

catch(error) {

alert(error.message);

}
};


// LOGIN

window.loginUser = async function () {

const email =
document.getElementById('loginEmail').value;

const password =
document.getElementById('loginPassword').value;


try {

const userCredential =

await signInWithEmailAndPassword(

auth,
email,
password
);

const user = userCredential.user;


// EMAIL VERIFY CHECK

if (!user.emailVerified) {

alert("Please verify email first");

return;
}


// GET ROLE

const querySnapshot = await getDocs(

query(

collection(db, "users"),

where("email", "==", email)

)

);


querySnapshot.forEach((doc) => {

const role = doc.data().role;
// alert("ROLE = " + role);

// ROLE REDIRECTS

if (role === "admin") {

window.location.href =
"/admin-dashboard/";
}

else if (role === "business") {

window.location.href =
"/business-dashboard/";
}

else if (
    role === "team_leader" ||
    role === "leader"
) {
 // alert("TEAM LEADER");
window.location.href =
"/leader/dashboard/";
}

else {

window.location.href =
"/employee-dashboard/";
}

});

}

catch(error) {

alert(error.message);

}
};


// LOGOUT

window.logoutUser = function () {

signOut(auth)

.then(() => {

window.location.href = "/";

});
};