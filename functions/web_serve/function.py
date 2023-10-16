import os
from azure.storage.blob import BlobServiceClient, BlobClient

import socket

import json
import base64
import time


def download_blob_new(blobName):
    blob_client = container_client.get_blob_client(blobName)
    blob_data = blob_client.download_blob()
    data_ = blob_data.readall()
    return data_

def upload_blob_new(blobName,container_client,value):
    # Assuming container_client is defined globally
    blob_client = container_client.get_blob_client(blobName)

    # Upload the blob data
    blob_client.upload_blob(value, overwrite=True)
    print("success")
    
def main(event):
    connection_string =   "DefaultEndpointsProtocol=https;AccountName=serverlesscache;AccountKey=O7MZkxwjyBWTcPL4fDoHi6n8GsYECQYiMe+KLOIPLpzs9BoMONPg2thf1wM1pxlVxuICJvqL4hWb+AStIKVWow==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client("artifacteval")
    blobName = "money.txt"
    money = event['money']
    money = str(money)
    blobName = "money.txt"
    upload_blob_new(blobName, container_client, money)
    return {"Money":"100"}
