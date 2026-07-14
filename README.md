# 🚀 LangChain Learning Repository

A comprehensive collection of **LangChain** examples, experiments, and mini-projects built while learning modern LLM application development.

This repository covers everything from working with Large Language Models (LLMs) to prompt engineering, chat models, embeddings, structured outputs, and output parsers.

---

## 📚 Topics Covered

- ✅ Working with LLMs
- ✅ Chat Models
- ✅ Prompt Templates
- ✅ Chat Prompt Templates
- ✅ Message Placeholders
- ✅ Embeddings
- ✅ Output Parsers
- ✅ JSON Output Parser
- ✅ Pydantic Structured Output
- ✅ Structured Responses
- ✅ Chat History
- ✅ Prompt Engineering
- ✅ Environment Variables
- ✅ LangChain Core Components

---

## 📁 Repository Structure

```
Langchain/
│
├── 1.LLMs/                # Basic LLM examples
├── 2.ChatModels/          # Chat model implementations
├── 3.EmbedModels/         # Embedding model examples
├── Prompt/                # Prompt engineering & templates
├── Struct_out/            # Structured output using Pydantic
├── out_parsers/           # Output parser examples
│
├── requirements.txt
├── test.py
└── README.md
```

---

## 🛠 Tech Stack

- Python 3.x
- LangChain
- LangChain Core
- Pydantic
- Hugging Face
- OpenAI Compatible APIs
- dotenv

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git

cd <repo-name>
```

Create a virtual environment

### Windows

```bash
python -m venv langenv
langenv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv langenv
source langenv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_api_key

OPENROUTER_API_KEY=your_api_key

HUGGINGFACEHUB_API_TOKEN=your_token

GOOGLE_API_KEY=your_api_key
```

Only include the variables required for the examples you're running.

---

## ▶️ Running Examples

Run any example directly:

```bash
python Prompt/example.py
```

or

```bash
python out_parsers/json_out_parser.py
```

or

```bash
python Struct_out/pydantic_.py
```

---

## 📖 Learning Objectives

This repository is intended for developers learning:

- LangChain fundamentals
- Prompt Engineering
- LCEL (LangChain Expression Language)
- Prompt Templates
- Chat Models
- Embedding Models
- Output Parsers
- Structured Output
- Pydantic Integration
- Building modular LLM applications

---

## 📌 Current Modules

### 🔹 LLMs

Examples demonstrating how to interact with language models using LangChain.

### 🔹 Chat Models

Working with conversational models and message-based interactions.

### 🔹 Embeddings

Generating vector embeddings and understanding embedding models.

### 🔹 Prompt Engineering

Different prompt templates and prompt construction techniques.

### 🔹 Structured Output

Generating reliable structured responses using Pydantic models.

### 🔹 Output Parsers

Parsing model responses into JSON and other structured formats.

---

## 📈 Future Additions

This repository will continue to expand with:

- Agents
- Tool Calling
- RAG (Retrieval-Augmented Generation)
- Memory
- LangGraph
- MCP Integration
- Vector Databases
- Multi-Agent Systems
- Streaming Responses
- Production-ready LangChain Applications

---

## 🤝 Contributions

Suggestions, improvements, and pull requests are always welcome.

If you discover a bug or have ideas for improving the examples, feel free to open an issue.

---

## 📄 License

This project is intended for educational purposes.

Feel free to use the code for learning and experimentation.

---

## ⭐ Support

If you found this repository useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future updates.
