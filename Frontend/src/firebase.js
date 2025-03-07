import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs } from 'firebase/firestore/lite';
import { getAuth } from "firebase/auth";
import 'firebase/compat/firestore';
import { GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBVGnfWCyKYocokgDPi_hGjVFoWKAU43Fw",
    authDomain: "metadata-ee971.firebaseapp.com",
    projectId: "metadata-ee971",
    storageBucket: "metadata-ee971.appspot.com",
    messagingSenderId: "101391171303",
    appId: "1:101391171303:web:5f19fe2751468318d36c42",
    measurementId: "G-HEDT1PEHML"
};

const app = initializeApp(firebaseConfig);

const db = getFirestore(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export { auth, provider, db };