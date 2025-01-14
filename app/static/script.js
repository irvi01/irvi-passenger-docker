const API_BASE = "http://localhost:8080";

let token = "";

// Registrar Usuário
document.getElementById("register-btn").addEventListener("click", async () => {
  const username = document.getElementById("register-username").value;
  const password = document.getElementById("register-password").value;

  const response = await fetch(`${API_BASE}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  alert(data.message || data.error);
});

// Login
document.getElementById("login-btn").addEventListener("click", async () => {
  const username = document.getElementById("login-username").value;
  const password = document.getElementById("login-password").value;

  const response = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  if (data.token) {
    token = data.token;
    document.getElementById("auth-token").textContent = `Token: ${token}`;
    alert("Login bem-sucedido!");
  } else {
    alert(data.error);
  }
});

// Criar Item
document.getElementById("create-item-btn").addEventListener("click", async () => {
  const name = document.getElementById("item-name").value;

  const response = await fetch(`${API_BASE}/items`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-access-token": token,
    },
    body: JSON.stringify({ name }),
  });

  const data = await response.json();
  if (data.id) {
    alert("Item criado!");
    fetchItems();
  } else {
    alert(data.error);
  }
});

// Listar Itens
async function fetchItems() {
  const response = await fetch(`${API_BASE}/items`, {
    method: "GET",
    headers: {
      "x-access-token": token,
    },
  });

  const items = await response.json();
  const list = document.getElementById("item-list");
  list.innerHTML = "";

  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item.name;

    const delBtn = document.createElement("button");
    delBtn.textContent = "Deletar";
    delBtn.addEventListener("click", () => deleteItem(item.id));

    li.appendChild(delBtn);
    list.appendChild(li);
  });
}

// Deletar Item
async function deleteItem(id) {
  await fetch(`${API_BASE}/items/${id}`, {
    method: "DELETE",
    headers: {
      "x-access-token": token,
    },
  });
  fetchItems();
}
