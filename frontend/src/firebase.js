import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAx-0fqDxw4Bnofay5-Q-m7kCJQvXxATOE",
  authDomain: "aplicacionesingambiental.firebaseapp.com",
  projectId: "aplicacionesingambiental",
  storageBucket: "aplicacionesingambiental.firebasestorage.app",
  messagingSenderId: "674489632860",
  appId: "1:674489632860:web:d8087bfa3e3979b6f53e99"
};

const app = initializeApp(firebaseConfig);

export const db = getFirestore(app);