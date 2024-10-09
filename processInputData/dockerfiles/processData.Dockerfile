# Use a imagem python:3.9-slim, que já tem Python 3.9 instalado
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Instalar Git, curl, xvfb, libgl1-mesa-glx e outras dependências
RUN apt-get update && apt-get install -y git curl xvfb libgl1-mesa-glx python3-tk python3-distutils

# Instalar pip (não precisa instalar Python 3.9 novamente)
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py

# Instalar o setuptools
RUN python -m pip install --upgrade setuptools

# Instalar as dependências do seu projeto
COPY neurolabkit /app/neurolabkit
RUN cd neurolabkit && python -m pip install -e .

# Copiar os scripts Python para o container
COPY pythonfiles/input.py .
COPY pythonfiles/output.py .
COPY pythonfiles/processing.py .

# Comando para rodar o script Python
CMD ["python", "input.py"]
