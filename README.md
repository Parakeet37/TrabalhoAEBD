# TrabalhoAEBD
Trabalho Prático de AEBD

###Base de dados
Para utilizar a api é preciso criar um tablespace e um user que lhe aceda.


######CRIAÇÃO DO TABLESPACE
```
create tablespace trabalho
datafile '\u01\app\oracle\oradata\orcl12\orcl\trabalho.dbf'
size 500M;
```


######CRIAÇÃO DO UTILIZADOR
```
create user adm
identified by wow
default tablespace trabalho
temporary tablespace temp
quota 450M on trabalho;
```


######PRIVILÉGIOS DO UTILIZADOR
```
GRANT CONNECT TO user1;
GRANT RESOURCE TO user1;
```


###Django
Para além de criar o tablespace e o utilizador, também é preciso instalar packages que foram necessários para a criação da api e para a conexão à base de dados

###Instalar Django
```
pip install django

######Instalar API Django REST-FRAMEWORK
```
pip install djangorestframework
```

######CX_ORACLE
```
pip install cx_oracle
```

###Instalar Oracle client
```
https://www.oracle.com/technetwork/database/enterprise-edition/downloads/database12c-win64-download-2297732.html

######CRIAR TABELAS NA BD
```
python manage.py makemigrations app
```

```
python manage.py migrate
```

######CRIAR SUPER USER DA BD PARA METER DUMMY DATA NA API PARA TESTAR
```
python manage.py createsuperuser
```
