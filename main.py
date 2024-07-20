from flask import Flask, request, render_template  # Import necessary modules from Flask

app = Flask(__name__)  # Create an instance of the Flask class

@app.route("/login", methods=["POST"])  # Define route for '/login' with POST method

def process():  # Define the function process to handle the '/login' route
  page = ""  # Initialize an empty string variable
  form = request.form  # Get the form data from the POST request

  if form["baldies"] == "david":  # Check if the 'baldies' field in the form equals 'david'
    page += f"You're alright {form['username']}"  # Append a success message to the page variable
  else:
    page += f"You've picked wrong {form['username']}"  # Append a failure message to the page variable

  return page  # Return the final page string


@app.route('/')  # Define route for the root URL

def index():  # Define the function index to handle the root URL
    return render_template('example.html')  # Render the 'example.html' template


app.run(host='0.0.0.0', port=81)  # Run the Flask application on host '0.0.0.0' and port 81