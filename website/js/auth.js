const google_signups =  document.querySelectorAll('#google-signup')

google_signups.forEach((signup)=>{
  signup.addEventListener("click",()=>{
    var provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth()
      .signInWithPopup(provider)
      .then((result) => {
        /** @type {firebase.auth.OAuthCredential} */
        var credential = result.credential;
    
        // This gives you a Google Access Token. You can use it to access the Google API.
        var token = credential.accessToken;
        // The signed-in user info.
        var user = result.user;
        window.location.href = "./discover.html"
        // ...
      }).catch((error) => {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // The email of the user's account used.
        var email = error.email;
        // The firebase.auth.AuthCredential type that was used.
        var credential = error.credential;
        // ...
      });
})
})


const google_signouts = document.querySelectorAll('#google-signout')

google_signouts.forEach((signout)=>{
  signout.addEventListener("click",()=>{
    console.log("c")
    firebase.auth().signOut()
    .then(()=>{
        window.location.href = "./index.html"
    })
    .catch((error)=>{
        console.log(error)
    })
})
})



// document.querySelector('#google-signout').addEventListener("click",()=>{
//     firebase.auth().signOut
//     .then(()=>{
//         window.location.href = "./index.html"
//     })
//     .catch((error)=>{
//         console.log(error)
//     })
// })