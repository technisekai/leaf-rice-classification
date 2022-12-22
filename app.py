from model.predict import *
from flask import Flask, render_template

# flask conf
app = Flask(__name__)

# index page
@app.route('/')
def home():
	return render_template('index.html', title="Home")

if __name__ == '__main__':
	app.run(debug=True)