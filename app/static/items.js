const API_BASE = "http://localhost:8080";
const token = localStorage.getItem("jwt");

// Verificar se o token está disponível
if (!token) {
  alert("Por favor, faça login para acessar esta página.");
  window.location.href = "index.html";
}

// Função para buscar e exibir itens
async function fetchAndDisplayItems() {
  const response = await fetch(`${API_BASE}/items`, {
    method: "GET",
    headers: { "x-access-token": token },
  });

  const items = await response.json();
  const tbody = document.querySelector("#items-table tbody");
  tbody.innerHTML = ""; // Limpar a tabela antes de adicionar novos itens

  items.forEach((item) => {
    const row = document.createElement("tr");

    const idCell = document.createElement("td");
    idCell.textContent = item.id;

    const nameCell = document.createElement("td");
    nameCell.textContent = item.name;

    row.appendChild(idCell);
    row.appendChild(nameCell);

    tbody.appendChild(row);
  });
}

// Chamar a função ao carregar a página
fetchAndDisplayItems();
