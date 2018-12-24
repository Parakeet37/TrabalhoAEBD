from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from app.models import ActiveSessions, PGA, Profiles, CPU, Tablespace, TablespaceHistory, Roles, SQLQuery, Users, SGA
from app.serializers import ActiveSessionsSerializer, PGASerializer, ProfilesSerializer, CPUSerializer, TablespaceSerializer, \
TablespaceHistorySerializer, RolesSerializer, SGASerializer, UsersSerializer, SQLQuerySerializer

# Create your views here.
class ActiveSessionsViewSet(viewsets.ViewSet):

    #procurar sessões ativas num determinado timestamp;
    #o timestamp vem no get
    #para implementar isto a bd tem de estar por sessão em vez de por contagem
    def retrieve(self, request):
        pass #a impementar depois, se der tempo

    #retornar a contagem das sessões por timestamp
    def list(self, request):
        sessions = ActiveSessions.objects.all()
        serializer = ActiveSessionsSerializer(sessions, many=True, context={"request": request})
        return Response(serializer.data)


class CPUViewSet(viewsets.ViewSet):

    #retornar a contagem dos cpus ativos por timestamp
    def list(self, request):
        cpus = CPU.objects.all()
        serializer = CPUSerializer(cpus, many=True, context={'request': request})
        return Response(serializer.data)


class TablespaceViewSet(viewsets.ViewSet):

    #retornar todos os tablespaces
    def list(self, request):
        tablespaces = Tablespace.objects.all()
        serializer = TablespaceSerializer(tablespaces, many=True, context={'request': request})
        return Response(serializer.data)

    #retornar o histórico de um tablespace
    def retrieve(self, request, tablespace):
        tablespace_obj = TablespaceHistory.objects.filter(tablespace_name=tablespace)
        serializer = TablespaceHistorySerializer(tablespace_obj, many=True, context={'request': request})
        return Response(serializer.data)


class ProfilesViewSet(viewsets.ViewSet):

    #retorna todos os profiles da bd
    def list(self, request):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class RolesViewSet(viewsets.ViewSet):

    #retorna todos os roles da bd
    def list(self, request):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True, context={'request': request})
        return Response(serializer.data)


class SQLQueryViewSet(viewsets.ViewSet):

    #retorna todas as queries dentro de um determinado espaço de tempo
    def retrieve(self,request):
        #a implementar se der tempo
        pass

    #retorna as últimas 500 queries feitas na bd
    def list(self, request):
        queries = SQLQuery.objects.all()
        serializer = SQLQuerySerializer(queries, many=True, context={'request': request})
        return Response(serializer.data)


class UsersViewSet(viewsets.ViewSet):

    #retorna um utilizador específico
    def retrieve(self, request, username):
        #a implementar se der tempo
        pass

    #retorna todos os utilizadores da bd
    def list(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)


class PGAViewSet(viewsets.ViewSet):

    #retorna todos os pga da bd
    def list(self, request):
        pga = PGA.objects.all()
        serializer = PGASerializer(pga, many=True, context={'request': request})
        return Response(serializer.data)


class SGAViewSet(viewsets.ViewSet):

    #retorna todos os sga da bd
    def list(self, request):
        sga = SGA.objects.all()
        serializer = SGASerializer(sga, many=True, context={'request': request})
        return Response(serializer.data)