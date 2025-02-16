FROM ollama/ollama

VOLUME ["/root/.ollama"]

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip

RUN pip install Flask

RUN pip install langchain langchain-community langchain-core beautifulsoup4 tiktoken chromadb langchain-ollama

COPY app.py /.
COPY main.py /.

EXPOSE 11434 8000

# CMD ["fastapi", "dev", "main.py"]

