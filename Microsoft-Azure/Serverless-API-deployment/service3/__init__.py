import logging
import random
import string
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    charList= []
    for i in range(5):
        charList.append(random.choice(string.ascii_letters))
    chars="".join(charList)
    return str(chars)
