# PDF Assistant Using Lamma2 (RAG - Project)

## Overview
This project is a Retrieval-Augmented Generation (RAG) application that enables users to ask questions about PDF documents using open-source LLMs. Built with Llama2, the application retrieves relevant information from uploaded PDFs and generates accurate, context-aware responses. It's an ideal proof-of-concept for integrating NLP with document querying for educational, research, or knowledge management purposes.

## Features
- **PDF Upload & Processing**: Upload and extract text from PDF files for efficient indexing and retrieval
- **Natural Language Q&A**: Ask questions about PDF content and receive AI-generated answers
- **Open-Source Stack**: Uses Llama2 for LLM capabilities without reliance on proprietary APIs
- **Vector Search**: Embeddings-based retrieval for semantic matching and accuracy
- **Streamlit UI**: Intuitive web interface for easy interaction
- **Error Handling**: Robust file processing with automatic cleanup

## Tech Stack
- **Language**: Python 3.8+
- **LLM**: Llama2 (via Ollama)
- **Libraries**:
  - LangChain - RAG pipeline orchestration
  - PyPDF2/PyPDFLoader - PDF text extraction
  - Ollama Embeddings - Vector embeddings
  - DocArrayInMemorySearch - Vector store
  - Streamlit - Web interface

## Installation

### Prerequisites
- Python 3.8+
- Ollama installed with `llama2` model
  - Download: [ollama.ai](https://ollama.ai)
  - Run: `ollama pull llama2`

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/harshsharma/Ragapplication.git
   cd Ragapplication
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser to `http://localhost:8501`

## Usage
1. **Upload PDF**: Click the upload area and select a PDF file
2. **Ask Question**: Enter your question in the text input (e.g., "What are the main topics?")
3. **Get Answer**: The app retrieves relevant sections and generates a response

## Project Structure
```
Ragapplication/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated: `source .venv/bin/activate` |
| Ollama connection error | Verify Ollama is running and `llama2` model is installed |
| Slow responses | Check system resources; Llama2 requires significant memory |
| PDF processing fails | Ensure PDF is not corrupted or password-protected |

## Future Enhancements
- Support for multiple document formats (DOCX, TXT, HTML)
- Chat history and conversation memory
- Custom model support and fine-tuning
- Performance optimization with caching
- Deployment via Docker

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
MIT License - feel free to use this project as a reference or starting point.

## Contact
For questions or collaboration opportunities, reach out via GitHub Issues.
