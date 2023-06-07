from flask import Flask, render_template, request
import os
from deeplearning import OCR

app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH, 'static/upload/')



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/service', methods=['POST','GET'])
def service():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        
       
            
        
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH, filename)
        upload_file.save(path_save)
        text = OCR(path_save,filename)
        
        return render_template('service.html',upload=True,upload_image=filename,text=text)
    
    return render_template('service.html',upload=False)


@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == "__main__":
    app.run(debug=True)