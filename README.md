# 🧠 LLM Docker Compose Project

Este projeto demonstra como executar uma aplicação Python que consome um modelo de linguagem (LLM) via API, utilizando dois containers Docker orquestrados com Docker Compose.

---

## 📁 Estrutura do Projeto

```
llm_project/
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
└── model/
    ├── Dockerfile
    └── main.py
```

---

## 🚀 Como Rodar

### 1. Requisitos

- Docker
- Docker Compose

### 2. Build e Up

Execute o seguinte comando na raiz do projeto:

```bash
docker compose up --build
```

> Isso iniciará dois containers:
> - `llm-model`: expõe uma API de geração de texto usando `transformers` (modelo GPT-2).
> - `python-app`: envia um prompt para o modelo e imprime a resposta.

### 3. Exemplo de Saída

```
Resposta gerada pelo modelo:
Era uma vez um mundo onde as máquinas aprendiam com os humanos e criavam histórias incríveis...
```

---

## 🧠 Sobre os Containers

### 🔹 `llm` (modelo)

- Imagem baseada em `python:3.10-slim`
- Usa Hugging Face Transformers e FastAPI
- Exposta na porta `8000`

### 🔹 `app` (cliente)

- Projeto Python simples com `requests`
- Faz POST para `http://llm:8000/generate`

---

## 🔧 Customização

Você pode substituir o modelo GPT-2 por outro, como:

```python
generator = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf")
```

> Atenção: modelos maiores exigem GPU e dependências específicas.

---

## 📄 Licença

Este projeto é livre para uso educacional e prototipação. Para modelos com licenças restritas (como LLaMA), verifique os termos oficiais.

---

## 🤝 Contribuições

Sugestões, melhorias e PRs são bem-vindos!
