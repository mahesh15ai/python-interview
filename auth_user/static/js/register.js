function validateForm() {
    let firstName = document.getElementById("first_name").value.trim();
    let lastName  = document.getElementById("last_name").value.trim();
    let username  = document.getElementById("username").value.trim();
    let email     = document.getElementById("email").value.trim();
    let password  = document.getElementById("password").value;

    let error = document.getElementById("client-error");

    // clear old error
    error.innerText = "";

    if (firstName === "" || lastName === "" || username === "" || email === "" || password === "") {
        error.innerText = "All fields are required";
        return false;
    }

    if (username.length < 4) {
        error.innerText = "Username must be at least 4 characters";
        return false;
    }

    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        error.innerText = "Please enter a valid email address";
        return false;
    }

    if (password.length < 6) {
        error.innerText = "Password must be at least 6 characters";
        return false;
    }

    return true; // allow form submit
}
