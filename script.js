document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulate login validation
    if (username === 'user' && password === 'pass') {
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('show-user-section').style.display = 'block';
        document.getElementById('show-username').innerText = username;
        document.getElementById('show-email').innerText = 'user@example.com'; // Simulated email
    } else {
        alert('Invalid credentials');
    }
});

document.getElementById('edit-user-button').addEventListener('click', function() {
    document.getElementById('show-user-section').style.display = 'none';
    document.getElementById('edit-user-section').style.display = 'block';

    // Pre-fill the form with current user data
    document.getElementById('edit-username').value = document.getElementById('show-username').innerText;
    document.getElementById('edit-email').value = document.getElementById('show-email').innerText;
});

document.getElementById('edit-user-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('edit-username').value;
    const email = document.getElementById('edit-email').value;

    // Simulate saving user data and email validation
    if (validateEmail(email)) {
        document.getElementById('edit-user-section').style.display = 'none';
        document.getElementById('show-user-section').style.display = 'block';
        document.getElementById('show-username').innerText = username;
        document.getElementById('show-email').innerText = email;
    } else {
        alert('Invalid email format');
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
