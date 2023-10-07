function validateForm() {
    // Get form input values
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    const rollnumber = document.getElementById("rollnumber").value;

    // Simple validation example (you can customize this)
    if (name.trim() === "") {
        alert("Please enter your name.");
        return false;
    }

    if (email.trim() === "") {
        alert("Please enter your email.");
        return false;
    }

    if (password.trim() === "") {
        alert("Please enter a password.");
        return false;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    if (rollnumber.trim() === "") {
        alert("Please enter your roll number.");
        return false;
    }

    alert("Registration successful!");
    return true;
}