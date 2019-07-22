import os

from flask import  Flask,flash, request, redirect, render_template
from werkzeug.utils import secure_filename


import pandas as pd

app=Flask(__name__)

	
@app.route('/')
def upload_form():
	return render_template('upload.html')


@app.route('/handleUpload', methods=['POST'])
def upload_file():
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join("/", filename))
		return render_template('complete.html')

if __name__=="__main__":
    app.run()
