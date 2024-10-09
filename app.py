from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)


# Importing Flask and render_template:
# Flask: This is the main class you will use to create your web application.
# render_template: This function is used to render HTML templates. It allows 
# you to return HTML files located in the templates folder of your project.

# Creating a Flask Application Instance:
# app is an instance of the Flask class. This instance represents your web 
# application.
# __name__ is passed to the Flask constructor to determine the root path for 
# the application. It helps Flask locate resources (like templates and static 
# files) relative to where this script is located.
    
# Defining a Route:
# @app.route('/'): This is a decorator that tells Flask what URL should 
# trigger the home function. The '/' route corresponds to the root URL of 
# your web application. 
# def home(): This defines a function named home. This function is executed 
# when the specified route is accessed.
# return render_template('index.html'): This line uses the render_template 
# function to return the content of index.html, which is located in the 
# templates folder. This HTML file will be rendered in the user's web browser.
    
# Running the Application:
# if __name__ == '__main__': This conditional checks if the script is being run directly (not imported as a module). If the script is being executed as the main program, the following block of code will run.
# app.run(debug=True): This line starts the Flask web server. The debug=True argument enables debug mode, which is useful during development. In debug mode:
# The server will automatically reload when code changes are detected.
# Detailed error messages will be displayed in the browser if there are any errors in your code.
    
# Summary of Functionality
# When you run this code, it starts a web server on your local machine (usually accessible 
# at http://127.0.0.1:5000).
# When a user visits the root URL (/), the Flask application calls the home function.
# The home function uses render_template to send back the index.html file to the user's web browser, rendering it as a webpage.
# Example of How It Works
# Starting the Server: You run python app.py in your terminal.
# Accessing the Application: You open your web browser and go to http://127.0.0.1:5000.
# Triggering the Route: The Flask server receives the request for the root URL and calls the home function.
# Rendering the Template: The home function returns index.html, which the browser displays to the user.
# Conclusion
# This code represents a basic structure for a Flask web application, illustrating how routes and 
# templates work together to serve web pages. If you have any more questions or want to delve deeper into 
# any specific part of the code, just let me know!