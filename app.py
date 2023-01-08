from model.predict import *
import os
from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

# flask conf
app = Flask(__name__)

# file upload configuration
UPLOAD_FOLDER = 'static/test_image/'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# validation file upload
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# index page
@app.route('/', methods=['POST', 'GET'])
def home():
	test_img, res_test_img = None, None
	if request.method == 'POST':
		test_img = request.files['test-img']
	if test_img and allowed_file(test_img.filename):
		test_img_filename = secure_filename(test_img.filename)
		test_img.save(os.path.join(app.config['UPLOAD_FOLDER'], test_img_filename))
		test_img = UPLOAD_FOLDER+test_img_filename
		res_test_img = predict(test_img)

	return render_template('index.html', result = res_test_img, title="Home")

if __name__ == '__main__':
	app.run(debug=True)