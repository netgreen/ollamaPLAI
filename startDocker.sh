#!/bin/sh

docker stop ollamaMistral
docker rm ollamaMistral
docker build -t ollama_last_build .
docker run -d --name ollamaMistral -p 11434:11434 ollama_last_build
docker exec -it ollamaMistral ollama run Mistral
