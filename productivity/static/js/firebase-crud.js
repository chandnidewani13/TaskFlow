import { initializeApp }

from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";

import {

getFirestore,

collection,

addDoc,

getDocs,

deleteDoc,

doc,

updateDoc

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

const db = getFirestore(app);


// CREATE TASK

window.createTask = async function () {

const title =
document.getElementById('taskTitle').value;

const priority =
document.getElementById('taskPriority').value;

const status =
document.getElementById('taskStatus').value;


await addDoc(collection(db, "tasks"), {

title: title,

priority: priority,

status: status,

createdAt: new Date()
});


alert("Task Created Successfully");
};


// FETCH TASKS

window.loadTasks = async function () {

const querySnapshot =

await getDocs(collection(db, "tasks"));

const taskContainer =
document.getElementById('taskContainer');

taskContainer.innerHTML = "";


querySnapshot.forEach((docItem) => {

const data = docItem.data();

taskContainer.innerHTML += `

<div class="card p-3 mb-3">

<h5>${data.title}</h5>

<p>${data.priority}</p>

<p>${data.status}</p>

</div>

`;
});
};