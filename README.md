# Book Recommendation

**Número da Lista**: X<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Aluno
|Matrícula | Aluno |
| -- | -- |
| 15/0122837  |  Davi Alves Bezerra |

## Sobre 
A ideia principal do projeto é fazer um sistema de recomendação de livros baseado em grafos.

No site oficial da amazon é possivel ver um exemplo de como funciona a recomendação.
A partir da busca de um livro, ele retorna para o usuario livros que a pessoa que comprou o livro buscado também comprou.

![image](https://user-images.githubusercontent.com/34287081/202867144-545e330c-d46f-4ef0-aaeb-62a6b13b130b.png)

Seguindo esse exemplo, em grafo não direcionado é possivel atráves dos componente conectados encontrar todos os nós é conectados por um caminho.
Sendo assim, uma pessoa que compra um livro tem conexões com outras pessoas que também o compraram e que compraram outros livros.

## Screenshots
É possivel a partir de um livro, ver quais outros livros que pessoas que o compraram também compraram.

![image](https://user-images.githubusercontent.com/34287081/202867523-34244edf-32e0-4824-8239-1bfa08bd8371.png)

Há como selecionar alguns parametros.

![image](https://user-images.githubusercontent.com/34287081/202867553-5366487d-5151-4cae-8231-81ca7c870667.png)

### Quantidade de dados para busca:
  Nesse slider é possivel escolher quantos dados da base de dados deseja ter na busca.
  
  ![image](https://user-images.githubusercontent.com/34287081/202867592-d54c2a7c-eb3a-40ba-9100-01b6cd5ea690.png)

  
### Como deseja que a recomendação seja feita:

  1 - por quantidade de pessoas que compraram
  
  2 - por quantidade de likes no livro
  
  ![image](https://user-images.githubusercontent.com/34287081/202867628-894741f8-0cb7-4c8a-98dc-b7df4f9fcc06.png)

### Quantidade de recomendações desejada
  Nesse slider é possivel selecionar quantos resultados deseja ver na tabela ao lado.
  
  ![image](https://user-images.githubusercontent.com/34287081/202867646-6e3507b7-fd44-4b34-ad3c-8ac5ceec8bc2.png)

  

## Instalação 
**Linguagem**: Python 3.8.13 <br>
**Framework**: Streamlit 1.15.0<br>

Para rodar o projeto, primeiro crie uma virtual env
```bash
pyenv virtualenv 3.8.13 book-recommendation
```

Ative a env
```bash
pyenv active book-recommendation
```

Instale as dependencias
```bash
pip install -r requirements.txt
```

Baixe o dataset
```bash
wget https://snap.stanford.edu/data/bigdata/amazon/amazon-meta.txt.gz
```

Extraia o dataset usando o `gzip`
```bash
gzip -dk amazon-meta.txt.gz
```

## Uso 
Agora para utilizar, basta rodar o `Streamlit`
```bash
streamlit run app.py
```




