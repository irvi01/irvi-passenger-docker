const API_BASE = "http://localhost:8080";

// Registrar os eventos dos botões após o DOM carregar completamente
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("register-btn").addEventListener("click", register);
    document.getElementById("login-btn").addEventListener("click", login);
  });
  

// Registrar Usuário
async function register() {
  const username = document.getElementById("register-username").value;
  const password = document.getElementById("register-password").value;

  const response = await fetch(`${API_BASE}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  alert(data.message || data.error);
}

// Login
async function login() {
  const username = document.getElementById("login-username").value;
  const password = document.getElementById("login-password").value;

  const response = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  if (data.token) {
    localStorage.setItem("jwt", data.token);
    alert("Login bem-sucedido!");
    window.location.href = "/static/crud.html";
  } else {
    alert(data.error);
  }
}
