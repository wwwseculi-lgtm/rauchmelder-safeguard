// Firebase Configuration for Secu.li
// HINWEIS: Der Benutzer muss ein eigenes Firebase-Projekt erstellen und diese Werte ersetzen

const firebaseConfig = {
    apiKey: "IHRE_API_KEY_HIER",
    authDomain: "secu-li.firebaseapp.com",
    projectId: "secu-li",
    storageBucket: "secu-li.appspot.com",
    messagingSenderId: "123456789",
    appId: "IHRE_APP_ID_HIER"
};

// Firebase SDK wird über CDN geladen
// Initialisierung erfolgt nach dem Laden der Seite

let auth;
let db;

// Firebase initialisieren wenn SDK geladen
function initializeFirebase() {
    if (typeof firebase !== 'undefined') {
        firebase.initializeApp(firebaseConfig);
        auth = firebase.auth();
        db = firebase.firestore();

        // Auth State Observer
        auth.onAuthStateChanged((user) => {
            if (user) {
                // Benutzer ist eingeloggt
                console.log('Benutzer eingeloggt:', user.email);
                updateUIForLoggedInUser(user);
            } else {
                // Benutzer ist nicht eingeloggt
                console.log('Kein Benutzer eingeloggt');
                updateUIForLoggedOutUser();
            }
        });
    }
}

// UI für eingeloggten Benutzer aktualisieren
function updateUIForLoggedInUser(user) {
    const authLinks = document.querySelectorAll('.auth-link');
    const userMenu = document.querySelectorAll('.user-menu');
    const userName = document.querySelectorAll('.user-name');

    authLinks.forEach(link => link.style.display = 'none');
    userMenu.forEach(menu => menu.style.display = 'flex');
    userName.forEach(name => name.textContent = user.displayName || user.email.split('@')[0]);
}

// UI für ausgeloggten Benutzer aktualisieren
function updateUIForLoggedOutUser() {
    const authLinks = document.querySelectorAll('.auth-link');
    const userMenu = document.querySelectorAll('.user-menu');

    authLinks.forEach(link => link.style.display = 'flex');
    userMenu.forEach(menu => menu.style.display = 'none');
}

// Registrierung mit E-Mail/Passwort
async function registerWithEmail(email, password, name) {
    try {
        const userCredential = await auth.createUserWithEmailAndPassword(email, password);

        // Benutzername setzen
        await userCredential.user.updateProfile({
            displayName: name
        });

        // Benutzer in Firestore speichern
        await db.collection('users').doc(userCredential.user.uid).set({
            name: name,
            email: email,
            createdAt: firebase.firestore.FieldValue.serverTimestamp(),
            appointments: [],
            maintenanceReminders: []
        });

        return { success: true, user: userCredential.user };
    } catch (error) {
        console.error('Registrierungsfehler:', error);
        return { success: false, error: getErrorMessage(error.code) };
    }
}

// Anmeldung mit E-Mail/Passwort
async function loginWithEmail(email, password) {
    try {
        const userCredential = await auth.signInWithEmailAndPassword(email, password);
        return { success: true, user: userCredential.user };
    } catch (error) {
        console.error('Anmeldefehler:', error);
        return { success: false, error: getErrorMessage(error.code) };
    }
}

// Anmeldung mit Google
async function loginWithGoogle() {
    try {
        const provider = new firebase.auth.GoogleAuthProvider();
        const result = await auth.signInWithPopup(provider);

        // Prüfen ob neuer Benutzer
        if (result.additionalUserInfo.isNewUser) {
            await db.collection('users').doc(result.user.uid).set({
                name: result.user.displayName,
                email: result.user.email,
                photoURL: result.user.photoURL,
                createdAt: firebase.firestore.FieldValue.serverTimestamp(),
                appointments: [],
                maintenanceReminders: []
            });
        }

        return { success: true, user: result.user };
    } catch (error) {
        console.error('Google-Anmeldefehler:', error);
        return { success: false, error: getErrorMessage(error.code) };
    }
}

// Passwort zurücksetzen
async function resetPassword(email) {
    try {
        await auth.sendPasswordResetEmail(email);
        return { success: true };
    } catch (error) {
        console.error('Passwort-Reset-Fehler:', error);
        return { success: false, error: getErrorMessage(error.code) };
    }
}

// Abmelden
async function logout() {
    try {
        await auth.signOut();
        window.location.href = 'index.html';
    } catch (error) {
        console.error('Abmeldefehler:', error);
    }
}

// Benutzer-Termine abrufen
async function getUserAppointments() {
    if (!auth.currentUser) return [];

    try {
        const doc = await db.collection('users').doc(auth.currentUser.uid).get();
        if (doc.exists) {
            return doc.data().appointments || [];
        }
        return [];
    } catch (error) {
        console.error('Fehler beim Abrufen der Termine:', error);
        return [];
    }
}

// Termin hinzufügen
async function addAppointment(appointment) {
    if (!auth.currentUser) return { success: false, error: 'Nicht eingeloggt' };

    try {
        const appointmentData = {
            ...appointment,
            id: Date.now().toString(),
            createdAt: firebase.firestore.FieldValue.serverTimestamp(),
            status: 'ausstehend'
        };

        await db.collection('users').doc(auth.currentUser.uid).update({
            appointments: firebase.firestore.FieldValue.arrayUnion(appointmentData)
        });

        // Auch in separater Collection für Admin-Übersicht
        await db.collection('appointments').add({
            ...appointmentData,
            userId: auth.currentUser.uid,
            userEmail: auth.currentUser.email,
            userName: auth.currentUser.displayName || auth.currentUser.email
        });

        return { success: true, appointment: appointmentData };
    } catch (error) {
        console.error('Fehler beim Hinzufügen des Termins:', error);
        return { success: false, error: error.message };
    }
}

// Wartungs-Erinnerung hinzufügen
async function addMaintenanceReminder(reminder) {
    if (!auth.currentUser) return { success: false, error: 'Nicht eingeloggt' };

    try {
        await db.collection('users').doc(auth.currentUser.uid).update({
            maintenanceReminders: firebase.firestore.FieldValue.arrayUnion({
                ...reminder,
                id: Date.now().toString(),
                createdAt: new Date().toISOString()
            })
        });
        return { success: true };
    } catch (error) {
        console.error('Fehler beim Hinzufügen der Wartungs-Erinnerung:', error);
        return { success: false, error: error.message };
    }
}

// Fehlermeldungen auf Deutsch
function getErrorMessage(errorCode) {
    const messages = {
        'auth/email-already-in-use': 'Diese E-Mail-Adresse ist bereits registriert.',
        'auth/invalid-email': 'Ungültige E-Mail-Adresse.',
        'auth/operation-not-allowed': 'Diese Anmeldemethode ist nicht aktiviert.',
        'auth/weak-password': 'Das Passwort muss mindestens 6 Zeichen lang sein.',
        'auth/user-disabled': 'Dieses Konto wurde deaktiviert.',
        'auth/user-not-found': 'Kein Konto mit dieser E-Mail-Adresse gefunden.',
        'auth/wrong-password': 'Falsches Passwort.',
        'auth/too-many-requests': 'Zu viele Versuche. Bitte versuchen Sie es später erneut.',
        'auth/popup-closed-by-user': 'Anmeldung abgebrochen.',
        'auth/network-request-failed': 'Netzwerkfehler. Bitte prüfen Sie Ihre Internetverbindung.'
    };
    return messages[errorCode] || 'Ein Fehler ist aufgetreten. Bitte versuchen Sie es erneut.';
}

// Prüfen ob Benutzer auf geschützter Seite eingeloggt ist
function requireAuth() {
    auth.onAuthStateChanged((user) => {
        if (!user) {
            window.location.href = 'login.html?redirect=' + encodeURIComponent(window.location.pathname);
        }
    });
}

// Firebase SDK laden und initialisieren
document.addEventListener('DOMContentLoaded', () => {
    // Warten bis Firebase geladen ist
    if (typeof firebase !== 'undefined') {
        initializeFirebase();
    } else {
        console.warn('Firebase SDK noch nicht geladen');
    }
});
