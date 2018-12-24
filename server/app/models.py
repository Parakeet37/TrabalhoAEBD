from django.db import models

#não é preciso criar id porque o django faz isso automaticamente e mete o como primary key
#se houver algum campo com "primary_key = true" não é criado id

# Create your models here.
class ActiveSessions(models.Model):
    count = models.IntegerField() #numero de sessoes ativas
    timestamp = models.DateTimeField() #timestamp da hora em que a informação foi tirada da bd

    class Meta:
        db_table = "activesessions"


class CPU(models.Model):
    sizeof = models.IntegerField() #numero de cpus ativos
    timestamp = models.DateTimeField() #timestamp da hora em que a info foi tirada da bd

    class Meta:
        db_table = "cpu"


class TablespaceModel(models.Model):
    tablespace_name = models.CharField(max_length=100) #nome do tablespace
    status = models.CharField(max_length=30) #disponibilidade do tablespace (online/offline)

    class Meta:
        abstract = True
        #isto faz com que não seja criada uma tabela na bd deste model,
        #apenas serve de base aos models que a importarem


class Tablespace(TablespaceModel):
    tablespace_inmb = models.IntegerField() #espaço total do tablespace
    freespace_inmb = models.IntegerField() #espaço livre do tablespace
    autoextensible = models.CharField(max_length=20) #se o tablespace é autoexpansível ou não
    file_name = models.CharField(max_length=100) #nome do datafile associado ao tablespace

    class Meta:
        db_table = "tablespace"


class TablespaceHistory(TablespaceModel):
    used = models.IntegerField() #percentagem de espaço usado
    timestamp = models.DateTimeField() #timestamp de hora em que a info foi tirada da bd

    class Meta:
        db_table = "tablespace_history"


class Profiles(models.Model):
    profile = models.CharField(primary_key=True, max_length=40) #nome do perfil

    class Meta:
        db_table = "profiles"


class Roles(models.Model):
    role = models.CharField(primary_key=True, max_length=120) #nome da função
    common = models.CharField(max_length=4) #se a função é comum ou não
    authentication_type = models.CharField(max_length=30) #tipo de autenticação

    class Meta:
        db_table = "roles"


class SQLQuery(models.Model):
    sql_fulltext = models.TextField() #query

    class Meta:
        db_table = "sql_query"


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=100) #nome do utilizador
    account_status = models.CharField(max_length=40) #estado da conta
    expiry_date = models.DateField() #data de fim da conta
    default_tablespace = models.CharField(max_length=100) #tablespace default do utilizador
    profile = models.CharField(max_length=30) #perfil do utilizador
    created = models.DateField() #data de criação do utilizador

    class Meta:
        db_table = "users"


class PGA(models.Model):
    name = models.CharField(primary_key=True, max_length=130) #nome do pga
    memory = models.IntegerField() #memória consumida

    class Meta:
        db_table = "pga"


class SGA(models.Model):
    pool = models.CharField(primary_key=True, max_length=20) #nome do sga
    memory = models.IntegerField() #memória livre

    class Meta:
        db_table = "sga"
