const API_BASE = "http://localhost:8080";
const token = localStorage.getItem("jwt");

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
