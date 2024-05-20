# Nome da imagem do Docker
IMAGE_NAME=ml-orquestrations-batch

# Caminho completo do volume
HOST_VOLUME_PATH=/home/gaspar/Modelos/ml-orquestrations-batch/plombery.db
CONTAINER_VOLUME_PATH=/app/plombery.db

# Target para construir a imagem Docker
build: ## Constrói a imagem Docker
	docker build -t $(IMAGE_NAME) .

# Target para rodar o contêiner Docker
run: ## Executa o contêiner Docker em segundo plano
	docker run -d -p 8001:8001 -v $(HOST_VOLUME_PATH):$(CONTAINER_VOLUME_PATH) --name $(IMAGE_NAME)_container $(IMAGE_NAME)

# Target para parar o contêiner Docker
stop: ## Para e remove o contêiner Docker
	docker stop $(IMAGE_NAME)_container || true
	docker rm $(IMAGE_NAME)_container || true

# Target para limpar as imagens e contêineres Docker
clean: ## Limpa as imagens e contêineres Docker
	make stop
	docker rmi $(IMAGE_NAME) || true
	docker system prune -f

# Target para formatar o código usando black
format: ## Formata o código na pasta src usando black
	black src

# Target para exibir a ajuda
help: ## Exibe esta mensagem de ajuda
	@echo "Escolha um alvo para executar:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: build run stop clean format help
