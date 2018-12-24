from rest_framework import serializers
from app.models import ActiveSessions, PGA, Profiles, CPU, Tablespace, TablespaceHistory, Roles, SQLQuery, Users, SGA


class ActiveSessionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActiveSessions
        fields = ('count', 'timestamp')


class CPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPU
        fields = ('sizeof', 'timestamp')


class TablespaceSerializer(serializers.ModelSerializer):

    used_space = serializers.SerializerMethodField('get_usedspace')

    class Meta:
        model = Tablespace
        fields = ('tablespace_name', 'tablespace_inmb', 'freespace_inmb', 'used_space', 'autoextensible', 'status', 'file_name')

    def get_usedspace(self, obj):
        return obj.tablespace_inmb - obj.freespace_inmb


class TablespaceHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TablespaceHistory
        fields = ('tablespace_name', 'used', 'status', 'timestamp')


class ProfilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profiles
        fields = ['profile']


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ('role', 'common', 'authentication_type')


class SQLQuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = SQLQuery
        fields = ('id', 'sql_fulltext')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('username', 'account_status', 'expiry_date', 'default_tablespace', 'profile', 'created')


class SGASerializer(serializers.ModelSerializer):

    class Meta:
        model = SGA
        fields = ('pool', 'memory')


class PGASerializer(serializers.ModelSerializer):

    class Meta:
        model = PGA
        fields = ('name', 'memory')