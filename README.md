# Arquivos e pastas

```
Project
│   README.md
│    data_to_mysql.py → arquivo responsável pela leitura dos dados obtidos por scrapping, criação do banco mysql e inserção dos dados.
│   requirements.txt → pacotes Python necessários.    
│
└───analysis_django
│   │   analysis_django → projeto Django criado para conter as aplicações.
│   │   app_{nome} → aplicação que contém a análise feita por {nome}.
│   │   app_home → página com algumas explicações, é direcionada pelo acesso à localhost:8000.
│   
│
│
└───db
│   │   notes_app.sql → dump do banco do dados que utilizamos para a análise.
│   │   schema.png → imagem do schema do banco.
│   │   schema.sql → script para criação do banco (lido pelo data_to_mysql).
│   
│
└───data
    │   disciplines.txt → disciplinas selecionadas para scrapping.
    │   texts.txt → textos obtidos por meio do scrapping das respectivas páginas das disciplinas na Wikipédia.
    
 
```

 # Para executar:

Clone o repositório:
``` console
  git clone ...
```
Baixe as dependências:
``` console
  pip3 install -r requirements.txt
```

Adicione a secret_key ao .env:
``` python
 SECRET_KEY = <secret_key>
```

No diretório que contém o arquivo manage.py:
``` console
  python3 manage.py runserver
```

 
  
