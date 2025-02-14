from django.db import models
from main.models import postgredb
import psycopg2
import asyncio
import json
from requests_oauthlib import OAuth1Session
from datetime import datetime
import requests

class PPD():
    def __init__(self):
        self.connn=postgredb()


    def lista(self):

        sql="""
        SELECT custrecord_ppdid, name, custrecord_ppd_productionline, custrecord_ppd_task, custrecord_ppd_vendor, custrecord_ppd_customer, custrecord_ppd_amountdollar, custrecord_ppd_amount, tranid, custbody_typepo, amount, statusref, recordn, custrecord_ppd_currency, trackingnumbers, trim(custbody_addtracking), custrecord_ppd_date, trandate, updated_at
	FROM public.ppd_detail;
        """
		
        data= self.connn.query(sql) 

        if data!=0:
            self.Nolista='0'
        else:
            self.Nolista='1'	

        return (data)

        


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
        SCRIPT_ID: int = 2506
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


    def refreshppd(self):

        self.connn=postgredb()

        listppd=self.lista()

        sql="""
        DELETE FROM ppd_detail
        """
        self.connn.update(sql)
        i=1

        for ppd in listppd:

            sql="""
            INSERT INTO ppd_detail    (
	                custrecord_ppdid, name,  custrecord_ppd_productionline, custrecord_ppd_task,  custrecord_ppd_date, custrecord_ppd_vendor, custrecord_ppd_customer, custrecord_ppd_currency, custrecord_ppd_amountdollar, custrecord_ppd_amount, tranid, custbody_typepo, amount, statusref, trandate,recordn,trackingnumbers,custbody_addtracking)  VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', 0{8}, 0{9}, '{10}', '{11}', 0{12}, '{13}', '{14}', '{15}','{16}','{17}')   
                """.format(ppd['custrecord_ppdid'], ppd['name'], ppd['custrecord_ppd_productionline'], ppd['custrecord_ppd_task'],ppd['custrecord_ppd_date'], ppd['custrecord_ppd_vendor'], ppd['custrecord_ppd_customer'], ppd['custrecord_ppd_currency'],ppd['custrecord_ppd_amountdollar'], ppd['custrecord_ppd_amount'], ppd['tranid'], ppd['custbody_typepo'], ppd['amount'], ppd['statusref'], ppd['trandate'], i, ppd['trackingnumbers'], ppd['custbody_addtracking'])
            self.connn.update(sql)
            i=i+1

        return self.res.json()
# Create your models here.
