#!/bin/sh

docker stop ollamaMistral
docker rm ollamaMistral
docker build -t ollama_last_build .
docker run -d --name ollamaMistral -p 11434:11434 -p 8000:8000 -v ollama_models:/root/.ollama ollama_last_build
