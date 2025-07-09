const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('arquivo_original');

// Criar elemento para mostrar o nome do arquivo e o botão de remover
const fileInfo = document.createElement('div');
fileInfo.style.marginTop = '10px';
dropArea.after(fileInfo);

function updateFileInfo() {
  fileInfo.innerHTML = '';
  if (fileInput.files.length > 0) {
    const fileName = fileInput.files[0].name;

    const span = document.createElement('span');
    span.textContent = fileName + ' ';

    const btnRemove = document.createElement('button');
    btnRemove.textContent = '❌';
    btnRemove.type = 'button';
    btnRemove.style.cursor = 'pointer';
    btnRemove.style.marginLeft = '10px';

    btnRemove.addEventListener('click', () => {
      fileInput.value = ''; // Limpa seleção
      updateFileInfo();
    });

    fileInfo.appendChild(span);
    fileInfo.appendChild(btnRemove);
  }
}

dropArea.addEventListener('click', () => fileInput.click());

dropArea.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropArea.classList.add('hover');
});

dropArea.addEventListener('dragleave', () => {
  dropArea.classList.remove('hover');
});

dropArea.addEventListener('drop', (e) => {
  e.preventDefault();
  dropArea.classList.remove('hover');
  const files = e.dataTransfer.files;
  if (files.length > 0) {
    fileInput.files = files;
    updateFileInfo();
  }
});

// Atualizar visualização se o usuário selecionar pelo input diretamente
fileInput.addEventListener('change', updateFileInfo);

// Inicializa (caso já tenha arquivo no input)
updateFileInfo();
