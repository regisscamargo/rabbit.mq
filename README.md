# Chat de Sistemas Distribuídos com RabbitMQ

Este repositório contém o código-fonte de um chat desenvolvido como parte de uma atividade da disciplina de Sistemas Distribuídos, ministrada na Universidade do Planalto Catarinense, no curso de Sistemas de Informação.

## Descrição

O chat implementado neste projeto é uma aplicação cliente-servidor que permite a comunicação entre múltiplos usuários em uma rede distribuída. Ele foi desenvolvido como parte de um estudo sobre conceitos fundamentais de sistemas distribuídos, incluindo comunicação entre processos, protocolos de rede e interfaces gráficas de usuário. O RabbitMQ é utilizado como o intermediário de mensagens para gerenciar a troca de mensagens entre os usuários.

## Funcionalidades

- **Login de Usuário:** Os usuários podem fazer login fornecendo um nome de usuário.
- **Chat em Grupo:** Os usuários podem enviar mensagens que serão distribuídas para todos os outros usuários conectados.
- **Mensagens Privadas:** Além do chat em grupo, os usuários podem enviar mensagens privadas diretamente para outro usuário, que só será visível para o destinatário.
- **Interface Gráfica:** A aplicação possui uma interface gráfica de usuário que facilita a interação e visualização das mensagens.

## Estrutura do Projeto

O projeto é dividido em duas partes principais:

- **Cliente:** Contém o código-fonte do cliente do chat, incluindo a interface gráfica de usuário e a lógica de comunicação com o servidor RabbitMQ.
- **Servidor:** Configuração do RabbitMQ para gerenciar as mensagens entre os clientes.

## Tecnologias Utilizadas

- **Python:** A linguagem de programação principal usada para implementar tanto o cliente quanto o servidor.
- **RabbitMQ:** Utilizado como broker de mensagens para gerenciar a comunicação entre os clientes.
- **Docker:** Para containerizar o RabbitMQ e facilitar sua execução e configuração.
- **PyQt:** Utilizado para criar a interface gráfica de usuário do cliente.

## Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.

### Passos para Executar

1. **Clone este repositório em sua máquina local:**
    ```sh
    git clone https://github.com/seu-usuario/chat-sistemas-distribuidos.git
    cd chat-sistemas-distribuidos
    ```

2. **Suba o servidor RabbitMQ usando Docker Compose:**
    ```sh
    docker-compose up -d
    ```

3. **Instale as dependências do cliente:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Execute o cliente:**
    ```sh
    python client.py
    ```

5. **Insira as informações de login no cliente e comece a enviar mensagens para o chat em grupo ou diretamente para outros usuários.**

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Este projeto foi desenvolvido como parte de uma atividade acadêmica por Régis Camargo.
