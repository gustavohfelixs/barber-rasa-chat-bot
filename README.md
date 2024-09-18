# RASA Barber Chatbot

Chatbot em RASA para atendimento de barbearia

# Instalação

Aqui estão os passos necessários para replicar o ambiente de desenvolvimento RASA no Windows

### Instalando WSL

```
wsl --update
wsl --set-default-version 2
wsl install --d ubuntu
```

### Instalação do Miniconda

1. Abra o terminal do Windows
2. Execute o seguinte comando:

- `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

3. Mova o arquivo baixado para a pasta home:
   Bash
   `mv Miniconda3-latest-Linux-x86_64.sh ~/`

Execute o seguinte comando:
Bash

```
bash ~/Miniconda3-latest-Linux-x86_64.sh
```

Siga as instruções na tela para concluir a instalação.

### Criando um ambiente virtual

1. Abra o terminal do Windows.
2. Execute o seguinte comando:
   Bash
   `conda create -n barber-chatbot python=3.9`
   ###### O detalhe do python=3.9 é muito importante para funcionar a insatalação do Rasa
3. Ative o ambiente virtual:
   Bash
   `conda activate barber-chatbot`

4. Instale pacotes no ambiente virtual:
   Bash
   `conda install numpy pandas matplotlib`

#### Para desativar o ambiente virtual:

`conda deactivate`

### Instale o RASA:

Use o comando
`pip3 install rasa.`

### Crie um projeto RASA:

Use o comando
`rasa init`

### Treine o modelo RASA: Use o

Utilize o comando dentro da pasta do projeto.
`rasa train`

### Teste o modelo RASA:

Use o comando
`rasa shell` dentro da pasta do projeto.
