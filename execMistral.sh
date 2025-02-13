#!/bin/sh

docker start ollamaMistral
docker exec -it ollamaMistral ollama run Mistral
