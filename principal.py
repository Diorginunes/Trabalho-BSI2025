from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/bsi')
def bis():
   return render_template('bsi.html')

@app.route('/sobre')
def sobre():
   return render_template('sobre.html')

# Run the application if this script is executed directly
if __name__ == '__main__':
   app.run(debug=True)