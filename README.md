# Conversor PDF ↔ DOCX

Uma aplicação web simples feita com Flask para converter arquivos entre PDF e DOCX (e ODT → PDF). 

## Funcionalidades

- Upload de arquivos `.pdf`, `.docx` e `.odt`
- Conversão automática:
  - PDF → DOCX
  - DOCX / ODT → PDF
- Interface simples com drag & drop para seleção do arquivo
- Exibição de mensagens de sucesso e erro
- Integração com Google AdSense para monetização (código exemplo)
  
## Tecnologias usadas

- Python 3
- Flask + Flask-WTF
- Biblioteca `pdf2docx` para conversão PDF → DOCX
- Biblioteca `docx2pdf` e LibreOffice para conversão DOCX/ODT → PDF
- JavaScript para drag & drop e controle do input file
- HTML5 + CSS para front-end minimalista

## Como usar

### Pré-requisitos

- Python 3.8 ou superior
- LibreOffice instalado (necessário para conversão de DOCX/ODT → PDF em Linux/Mac)
- Instale as dependências:

```bash
pip install -r requirements.txt
```

## Rodando localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/conversor-pdf-docx.git
cd conversor-pdf-docx
```

2. Configure variáveis secretas (por segurança, não deixe chaves fixas no código)

3. Execute o app Flask:
```bash
python app.py
```

4. Acesse http://localhost:5000 no navegador.

## Upload e conversão

    . Arraste ou selecione o arquivo PDF, DOCX ou ODT

    . Insira o nome desejado para o arquivo gerado (sem extensão)

    . Clique em "Converter"

    . O arquivo convertido será salvo no servidor (pasta uploads) e você verá mensagens de sucesso ou erro

## Atenção !!!

Por questões de segurança e privacidade, o download automático direto para a pasta Downloads do usuário não é possível via navegador. A aplicação atualmente salva o arquivo no servidor. Para baixar, você pode implementar rotas adicionais para enviar o arquivo ao cliente.

Remova informações sensíveis como SECRET_KEY e IDs do Google AdSense antes de publicar.

## Estrutura do projeto

```
/
├── app.py            # Código principal Flask
├── templates/
│   └── index.html    # Página HTML com formulário e anúncios
├── static/
│   ├── css/
│   └── scripts/
├── utils/
│   ├── docx_to_pdf.py
│   ├── pdf_to_docx.py
│   └── secret.py     # Geração de chaves secretas
├── uploads/          # Pasta onde os arquivos são salvos
└── requirements.txt  # Dependências Python
```

# Contribuindo

Contribuições são bem-vindas! Pode abrir issues, sugerir melhorias ou enviar pull requests.
