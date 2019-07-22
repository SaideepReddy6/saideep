from flask import  Flask,flash, request, redirect, render_template
app=Flask(__name__)
def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
@app.route('/')
def upload_form():
	import os
	from azure.storage.blob import BlockBlobService, PublicAccess
	from azure.storage.blob import BlockBlobService
	from flask import  Flask,flash, request, redirect, render_template
	from werkzeug.utils import secure_filename
	import pandas as pd
	import string, random, requests
	return render_template('upload.html')
@app.route('/handleUpload', methods=['POST'])
def upload_file():
	import os
	from azure.storage.blob import BlockBlobService, PublicAccess
	from azure.storage.blob import BlockBlobService
	from flask import  Flask,flash, request, redirect, render_template
	from werkzeug.utils import secure_filename
	import pandas as pd
	import string, random, requests
        file = request.files['file']
        filename = secure_filename(file.filename)
        #fileextension = filename.rsplit('.',1)[1]
        #Randomfilename = id_generator()
        #filename = Randomfilename + '.' + fileextension
        #file.save(os.path.join("upload/", filename)) 
        local_path=os.path.abspath(os.path.curdir)
        local_file_name=filename
        full_path_to_file =os.path.join(local_path, local_file_name)
        block_blob_service = BlockBlobService(account_name='sqlva4gk6bb2el7ldy', account_key='FWBELIECAHFMefpP2asx7SUV9ti72G9/xbBebJonNLY4C2JC5J4Ddf7vXnH+79AwmFfUfpwG3gqDz10zOffDhg==')
        container_name ='sdr'
        block_blob_service.create_container(container_name)
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)
        block_blob_service.create_blob_from_path(container_name, filename, full_path_to_file)
        return render_template('complete.html')
if __name__=="__main__":
    app.run()
