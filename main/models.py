from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db import models
import psycopg2
from datetime import datetime
import json
import sys
from django.conf import settings
import socket

# Create your models here.

class   postgredb():

    def __init__(self):

        self.host = settings.DATABASES['default']['HOST']
        self.database = settings.DATABASES['default']['NAME']
        self.user = settings.DATABASES['default']['USER']
        self.password = settings.DATABASES['default']['PASSWORD']
        self.port = settings.DATABASES['default']['PORT']
        try:
            self.connection = psycopg2.connect(database = self.database,  user = self.user, host= self.host, password = self.password, port = self.port)
        except psycopg2.DatabaseError:
            sys.exit('Failed to connect to database')

    def query(self,sql):
        results = []

        try:
            
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                dbRecord = cursor.fetchall()

                if dbRecord == None:
                    print('ERROR: First record not found', file=sys.stderr)
                else:
                    results=dbRecord
                dbRecordId = dbRecord[0]
                self.connection.commit()
                cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return results

    def update(self,sql):

        try:
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                self.connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit(1)

    def insertar(self,sql):

        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(sql)
                self.connection.commit()
                cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return()
