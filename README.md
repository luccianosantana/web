# Como utilizar

1 -  Crie uma pasta onde deseja colocar a aplicação:
     Exemplo C:\temp\desenv\django

2 - Vá para a pasta:
    cd C:\temp\desenv\django

3 - Criei um ambiente virtual python para a apliação:
    python -m venv venv

4 - Entre na pasta criada "venv"
    cd C:\temp\desenv\django\venv

5 - Clone o conteudo o git  
    git clone https://github.com/luccianosantana/web.git

6 - Inicie o ambiente virtual
    C:\temp\desenv\django\venv\Scripts\activate.bat

7 - Instalar o Django e dependencias:
    (venv) C:\temp\desenv\django\venv>pip install django
    (venv) C:\temp\desenv\django\venv>pip install django-bootstrap-form 
    (venv) C:\temp\desenv\django\venv>pip install django django-mysql

8 - Iniciar o projeto:
    (venv) C:\temp\desenv\django\venv>python manage.py runserver 80


Abra no navegador o endereço:  http://127.0.0.1/inventario    



