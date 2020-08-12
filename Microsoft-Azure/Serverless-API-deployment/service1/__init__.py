import logging
import azure.functions as func
import random
import requests
import os
from azure.cosmos import exceptions, CosmosClient, PartitionKey



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    endpoint = os.environ["uri"]
    key = os.environ["pkey"]

    client = CosmosClient(endpoint, key)

    database_name = 'usernames'
    database = client.create_database_if_not_exists(id=database_name)
    container_name = 'usernameStorage'
    container = database.create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path="/id"), offer_throughput=400)

    getletters = requests.get('https://agris123.azurewebsites.net/api/service3?code=AfwsKOwVIblqhzmcOVH4IJxaFQ0eMIiNQdsA1RnWaIHtqQKICUbL3w==')
    getnumbers = requests.get('https://agris123.azurewebsites.net/api/service2?code=LZAj225WWasaZLmUIOTMrpoeWOIMxQrwqir2TtFLdhiP8ufPqjKgTw==')
    letters = getletters.text   
    numbers= getnumbers.text
    answer = []
    for i in range(5):
        answer.append(letters[i])
        answer.append(numbers[i])
    ans="".join(answer)

    ansItem = {'id': ans}
    container.create_item(body=ansItem)

    return str(ans)