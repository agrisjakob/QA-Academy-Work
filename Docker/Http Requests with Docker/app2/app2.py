#- application 2:
#	- running on port 5001
#	- no web pages displayed
#	- animal route which returns the name of an animal in either text or json form
#	- noise route which takes a given animal and returns their noise in either text or json form

from flask import Flask, Response, request
import random
import requests
app = Flask(__name__)

@app.route('/animal', methods=['GET'])
def animal():
    animalList= ["dog", "cat", "chicken"]
    choice = random.choice(animalList)
    return Response(choice, mimetype='text/plain')

@app.route('/noise', methods=['GET', 'POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "dog":
        noise = "woof"
    elif animal == "cat":
        noise = "meow"
    elif animal == "chicken":
        noise = "bwuk"
    else:
        noise = "no animal selected"
    return Response(noise, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True,port=5001, host='0.0.0.0')
