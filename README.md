docker compose down

docker compose up --build  (very first time) and next times use below

docker compose up

docker compose exec ollama ollama pull translategemma:latest







docker compose exec:
This is a Docker Compose command that lets you run a command inside a running container (without needing to open an interactive shell like with docker compose exec -it ... bash).
Syntax: docker compose exec <service-name> <command-to-run-inside-the-container>
Here: ollama is the service name from your docker-compose.yml file (the Ollama server container).

ollama (the first one after exec)
This is the service/container name you're targeting.
Docker Compose looks for the container named something like languagetranslation-ollama-1 (or whatever your project prefix is), but you refer to it by the short service name ollama.

ollama pull translategemma:latest (the actual command executed inside the container)
This is the real Ollama CLI command.
ollama = the Ollama command-line tool (installed inside the ollama/ollama Docker image).
pull = Ollama subcommand that downloads a model from Ollama's registry (library.ollama.com) to your local machine (inside the container's storage).
translategemma:latest = the model identifier you want to download.
translategemma = the model family name (Google's open-source translation model series, released around Jan 2026, based on Gemma 3).
:latest = the tag (version/alias). It currently points to the 4B parameter version (~3.3 GB download size, supports 55 languages + vision input, 128K context).
Other tags exist like :4b, :12b, :27b if you want a different size.