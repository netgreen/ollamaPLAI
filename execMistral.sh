#!/bin/sh

docker start ollamaMistral
docker exec -it ollamaMistral ollama pull nomic-embed-text
docker exec -it ollamaMistral ollama pull Mistral
docker exec -it ollamaMistral python3 app.py
