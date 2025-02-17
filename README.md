# Ollama private local AI

## Prerequisites

Before installing, make sure you have the following tools installed:

- **Docker**: Install Docker from [docker.com](https://www.docker.com/)

## Pull Repo
```bash
gh repo clone netgreen/ollamaPLAI
```

## Mistral private and local AI
### Install the Container
```bash
./mistralInstall.sh
```
### pull and start Mistral
```bash
./execMistral.sh
```

## How to chat with the AI?
### Set REG Text
```bash
 curl -X POST http://localHost:8000/setRegText -H "Content-Type: application/json" -d '{"regText": "I am going to tell you a story about Avi."}'
```

### Ask a Question
```bash
curl -X POST http://localHost:8000/askQuestion -H "Content-Type: application/json" -d '{"question": "Who are you going to tell me a story about today?"}'
```
