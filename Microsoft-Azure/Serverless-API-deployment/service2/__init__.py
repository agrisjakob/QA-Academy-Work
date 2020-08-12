import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numberList= []
    for i in range(5):
        numberList.append(str(random.randint(0,9)))
    numbers=str("".join(numberList))
    return str(numbers)