# Usa uma imagem base Python oficial, versão 3.9 (slim para um ambiente mais leve)
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip cache purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copia todo o conteúdo do diretório atual para o diretório de trabalho do container
COPY . .

# Define o diretório /app no PYTHONPATH
ENV PYTHONPATH=/app

# Define o arquivo principal da aplicação Flask
ENV FLASK_APP=todo_project.run

# Expõe a porta 5000 para permitir que a aplicação Flask receba conexões
EXPOSE 5000

# Copia o script de entrada (entrypoint) para o container e dá permissões de execução
RUN chmod +x start/entrypoint.sh

# Define o script de entrada do container
CMD ["start/entrypoint.sh"]
