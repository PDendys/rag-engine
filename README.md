# RAG Engine

Python-based RAG engine service providing embeddings generation, auto-tagging, and reranking capabilities for retrieval-augmented generation systems. Available via REST API.

## Features

- **Reranking**: Advanced document reranking using state-of-the-art models
- **Embeddings Generation**: Convert text to high-dimensional vector embeddings
- **Auto-tagging**: Automatic content classification and tagging
- **REST API**: Easy integration via HTTP endpoints

## Installation

### Using Docker (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd rag-engine

# Build the Docker image
docker build -t embeddings-service:2025-10-06 .

# Run with Docker Compose
docker-compose up

# Or run detached
docker-compose up -d
```

## Usage

### Start the server

```bash
# Run with Docker Compose
docker-compose up

# Or run detached
docker-compose up -d
```

### Stop the service

```bash
# Stop Docker Compose
docker-compose down

# Or stop local development with Ctrl+C
```

### API Endpoints

```bash
# Embedding
POST /embedding/create

# Reranking
POST /reranker/rerank

# Auto tagger
GET /auto-tagger/tag
```

## Project Structure

```
rag-engine/
├── app/
│   ├── routes/           # API route definitions
│   ├── services/         # Business logic services
│   ├── constants.py      # Application constants
│   └── main.py          # FastAPI application entry point
├── requirements.txt      # Python dependencies
└── README.md            # This file
```