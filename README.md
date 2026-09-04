# 🤖 Agente de PDF com Agno + RAG

Agente de Inteligência Artificial capaz de consultar e responder perguntas com base no conteúdo de um documento PDF utilizando **RAG (Retrieval-Augmented Generation)**.

O projeto foi desenvolvido com **Agno**, **AgentOS**, **Claude (Anthropic)**, **ChromaDB**, **FastEmbed** e **Streamlit**, com deploy do backend e frontend utilizando **Render**.

---

## 🚀 Demo

### 🌐 Aplicação Web

Acesse a aplicação:

👉 https://primeiro-agente-com-agno-streamlit.onrender.com/

### ⚙️ AgentOS / Backend

Backend publicado no Render:

👉 https://agno-api-tz9e.onrender.com/

### 📚 Repositório

Código-fonte:

👉 https://github.com/FelipeVadao/Primeiro_Agente_Com_Agno

---

## 🧠 Sobre o projeto

Este projeto implementa um agente capaz de consultar informações presentes em um PDF e utilizar essas informações para gerar respostas contextualizadas.

O documento utilizado no projeto é o:

**Relatório Trimestral 2T25 — Grendene**

Em vez de depender apenas do conhecimento geral do modelo de linguagem, o agente realiza uma busca na base de conhecimento criada a partir do PDF.

Isso permite que as respostas sejam baseadas especificamente no conteúdo do documento.

---

## 🔎 O que é RAG?

**RAG (Retrieval-Augmented Generation)** é uma arquitetura que combina:

1. Recuperação de informações relevantes.
2. Geração de respostas utilizando um modelo de linguagem.

Neste projeto, o fluxo é:

```text
PDF
 ↓
PDFReader
 ↓
Divisão do conteúdo em documentos/chunks
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Busca semântica
 ↓
Contexto relevante
 ↓
Claude
 ↓
Resposta