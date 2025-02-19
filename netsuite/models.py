from django.db import models
import psycopg2
import asyncio
import json
from requests_oauthlib import OAuth1Session
from datetime import datetime
import requests
import base64
from django.conf import settings
import sys



class   postgredb():

    def __init__(self):

        self.host = 'localhost'
        self.database = 'ecd_database'
        self.user = 'postgres'
        self.password = 'gabc3150'
        self.port = '5432'
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

class Class_NetSuite():
   
    def __init__(self):
        
       # CLIENT_KEY: str = "adb62c969e3de81813105bcbdf1371f9741671ccfc7909ab162e24f1588ad4ad"
       # CLIENT_SECRET: str = "d537386d481f643eed5aea50b509a7af94977e610b5028143613d9bad58726e4"
       # ACCESS_KEY: str = "8b3f30d99c0fd7775a1532adbf9cbe1cbd9110b0902134091402817e6f1a274b"
       # ACCESS_SECRET: str = "abee94967d0834e36f560cf636badf9beb0df0b082b8e2e3275cb41134731746"

        CLIENT_KEY: str = "0c1e2737ef250097222db9624e19b265713f38bf15ff933bb4d4a343be1fba31"
        CLIENT_SECRET: str = "6e91b26dbee2fc12bde3bf12c9cacf9c1321b49659019534f6b76cbb635c9052"
        ACCESS_KEY: str = "bb67fbcb3d7724d387c5864c5531fe87e20e3314b222dce6511baa62b72821c8"
        ACCESS_SECRET: str = "5281c2088e4b5f6094e3931249390107d5ee8e603a7170289538ce5c32fe1f66"


        SIGNATURE_METHOD: str = "HMAC-SHA256"
        REALM_ID: str = "5896209"
        SCRIPT_ID: int = 2510
        DEPLOY_ID: int = 1
        URL: str = f"https://{REALM_ID}.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script={SCRIPT_ID}&deploy={DEPLOY_ID}"

        oauth = OAuth1Session(
            client_key=CLIENT_KEY,
            client_secret=CLIENT_SECRET,
            resource_owner_key=ACCESS_KEY,
            resource_owner_secret=ACCESS_SECRET,
            realm=REALM_ID,
            signature_method=SIGNATURE_METHOD
            )

        data = '{    "recordtype": "N/A",    "id": "55554u4445"}'

        headers = {
            "Content-Type": "application/json"
        }

        self.res = oauth.post(URL, data=json.dumps(data), headers=headers)


    def lista(self):

        return self.res.json()


    def refreshdp(self):

        self.connn=postgredb()

        listnetsuite=self.lista()

        sql="""
        TRUNCATE TABLE dispatch_plan
        """
        self.connn.update(sql)
        i=1

        for det in listnetsuite:

            taskdec = det['task_sc'].replace("&gt;", ">")
            memo = det['memo'].replace("'", " ")
           

            sql="""
            INSERT INTO public.dispatch_plan(
	        productionline, section, task_sc_id, task_sc, task_sc_enddate, tranid, trandate, altname, quantitycommitted, quantitytransfered, itemdleft, quantitybo, recordn, totalitemsbo, invoicedate, memo, item, item_id, dateformula, wo_id,so_id,ecd_model,productionlineid,customer_id)
	        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '0{8}', '0{9}', '{10}', '{11}', '{12}', '0{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}','{20}','{21}','{22}','{23}')""".format(det['productionline'], det['section'], det['task_sc_id'], taskdec,det['task_sc_enddate'], det['tranid'], det['trandate'], det['altname'], det['quantitycommitted'], det['quantitytransfered'], det['itemsleft'], det['quantitybo'], i , det['totalitemsbo'], det['invoicedate'],memo, det['item'], det['item_id'], det['dateformula'], det['wo_id'], det['so_id'], det['ECD_Model'], det['productionlineid'], det['customer_id']) 

            self.connn.update(sql)
            i=i+1

        return self.res.json()
# Create your models here.