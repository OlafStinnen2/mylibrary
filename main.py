from flask import Flask  # Import Flask class

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')  # Define the route for the main page

def index():  # Function to handle requests to the main page
  myName = "Olaf"  # Define a variable for the name to be used in the HTML page
  page = ""  # Initialize the variable to hold the HTML page content
  f = open("index.html", "r")  # Open the HTML file in read mode
  page = f.read()  # Read the contents of the file into the 'page' variable
  f.close()  # Close the HTML file
  page = page.replace("{name}", myName)  # Replace the placeholder with the actual name
  return page  # Return the modified HTML page

app.run(host='0.0.0.0', port=81)  # Run the Flask app on the specified host and port