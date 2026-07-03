import { initializeApp }

from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";

import {

getStorage,

ref,

uploadBytes

}

from "https://www.gstatic.com/firebasejs/10.12.2/firebase-storage.js";


const firebaseConfig = {

apiKey: "AIzaSyCGAC8n3GRe4AX_As_BSCJb8wLpg62IH6s",

authDomain: "fomca0006-internship.firebaseapp.com",

projectId: "fomca0006-internship",

storageBucket: "fomca0006-internship.firebasestorage.app",

messagingSenderId: "565201524954",

appId: "1:565201524954:web:8c5ef31b28ae1b781e6de3"
};


const app = initializeApp(firebaseConfig);

const storage = getStorage(app);


window.uploadFile = async function () {

const file =

document.getElementById('fileInput')

.files[0];


const storageRef =

ref(storage, 'uploads/' + file.name);


await uploadBytes(

storageRef,

file
);

alert("File Uploaded Successfully");
};