const API_BASE = "http://localhost:8080";
const token = localStorage.getItem("jwt");

try {
  const payload = JSON.parse(atob(token.split(".")[1]));
  const isTokenExpired = payload.exp * 1000 < Date.now();
  if (isTokenExpired) {
    alert("Token expirado. Por favor, faça login novamente.");
    window.location.href = "index.html";
  }
} catch (error) {
  alert("Token inválido. Por favor, faça login novamente.");
  window.location.href = "index.html";
}

// Verifique se o token está presente
if (!token) {
  alert("Por favor, faça login para acessar esta página.");
  window.location.href = "index.html"; // Redireciona para a página de login
}

// Mostre o token na interface (opcional)
document.getElementById("jwt-token").textContent = token;

// Criar Item
async function createItem() {
  const name = document.getElementById("create-item-name").value;

  const response = await fetch(`${API_BASE}/items`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-access-token": token,
    },
    body: JSON.stringify({ name }),
  });

  const data = await response.json();
  alert(data.message || data.error);
}

// Listar Itens
async function listItems() {
  const response = await fetch(`${API_BASE}/items`, {
    method: "GET",
    headers: { "x-access-token": token },
  });

  const items = await response.json();
  const list = document.getElementById("items-list");
  list.innerHTML = "";

  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = `ID: ${item.id} - Nome: ${item.name}`;
    list.appendChild(li);
  });
}

// Atualizar Item
async function updateItem() {
  const id = document.getElementById("update-item-id").value;
  const name = document.getElementById("update-item-name").value;

  const response = await fetch(`${API_BASE}/items/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "x-access-token": token,
    },
    body: JSON.stringify({ name }),
  });

  const data = await response.json();
  alert(data.message || data.error);
}

// Deletar Item
async function deleteItem() {
  const id = document.getElementById("delete-item-id").value;

  const response = await fetch(`${API_BASE}/items/${id}`, {
    method: "DELETE",
    headers: { "x-access-token": token },
  });

  const data = await response.json();
  alert(data.message || data.error);
}
