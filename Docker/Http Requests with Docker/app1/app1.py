#- application 1:
#	- running on port 5000
#	- home page with a button/link which takes you to a generate page
#	- generation page with route which makes a get request to a route in application 2 for an animal 
#	then posts that animal to another route in application 2 which responds with the animal noise.
#	Both the animal and their noise then need to be displayed on the web page.

from flask import Flask, Response, request, render_template, url_for
import requests
app = Flask(__name__)
api = 'http://app2:5001'

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    getanimal = requests.get(api + '/animal')
    animal = getanimal.text
    getnoise = requests.post(api + '/noise', animal)
    noise = getnoise.text
    return render_template('generate.html', animal=animal, noise=noise)


if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
