# Mensageria utilizando RabbitMQ e Python

Esse projeto foi desenvolvido para uma apresentação em grupo sobre Mensageria no IFPR - Campus Londrina.

Colaboradores/Integrantes do projeto: [Mateus Bolotaro](https://github.com/mbolotaro), [Fábio Araujo](https://github.com/Fabio-arbr), [Guilherme Mattos](https://github.com/guilherme-mattos-conde) 

### 👨‍🔧 Problema
Dentro de uma grande empresa, há uma necessidade de realizar um pequeno processamento de vários lotes de chaves PIX aleatórias que estão cadastradas no sistema dessa empresa.

As chaves devem ser lidas e delas devem ser extraidas uma informação: o email de quem vai receber o dinheiro.

Junin tentou fazer o processamento desses lotes por meio de requisições HTTP, ou seja, era enviado um lote para o servidor, e Junin deveria ficar esperando todo o lote ser processado. Essa requisição demorava muito tempo, e caso a conexão de uma das partes caísse, todo o processamento seria em vão.

Portanto, sua tarefa será implementar uma fila que deverá processar esses dados de forma assíncrona, enviá-los para uma outra fila (que será utilizada por outro serviço), e salvá-los localmente em um arquivo .txt. O formato dos dados no arquivo e na fila deve ser esse:

```{email}, {nome}, {cidade} - {chave_pix}```

##### Observações
- Outras informações, como o nome e cidade do destinatário também podem ser adquiridas (seria interessante salvá-las também, mas não obrigatório).
- Todas as chaves PIX aleatórias estão linkadas a um email, pelo menos por enquanto.

### 👨‍💻 Código
O código que será desenvolvido pela turma será o que se encontra no arquivo `main.py`.

Os arquivos `pix_generator.py` e `populator.py` são responsáveis por gerar e popular a fila, respectivamente.

Fique a vontade para realizar qualquer contribuição a esse projeto, basta abrir uma PR e detalhar suas implementações!

### 🚀 Como rodar

Primeiramente, você clonar este repositório, utilizando o comando:

```bash
git clone https://github.com/https-eduardo/messaging-tutorial.git
```
Em seguida, você deve instalar as bibliotecas necessárias utilizando o comando:
```bash
pip install -r requirements.txt
```
Se você já estiver com o RabbitMQ rodando, você já pode rodar o projeto, caso queira popular a fila, rode o `populator.py`, caso queira adicionar um consumidor a fila, rode o `consumer.py`.

```bash
py populator.py
```