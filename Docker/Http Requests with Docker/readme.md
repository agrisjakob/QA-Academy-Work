# application 1:
	- running on port 5000
	- home page with a button/link which takes you to a generate page
	- generation page with route which makes a get request to a route in application 2 for an animal 
	then posts that animal to another route in application 2 which responds with the animal noise.
	Both the animal and their noise then need to be displayed on the web page.


# application 2:
	- running on port 5001
	- no web pages displayed
	- animal route which returns the name of an animal in either text or json form
	- noise route which takes a given animal and returns their noise in either text or json form
