from flask import Flask,render_template,Response,request
import os
import cat_dog
import warnings
warnings.filterwarnings('ignore')


app=Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

bicycle = os.path.join(app.config['UPLOAD_FOLDER'],'bicycle.jpg')

@app.route('/')
def hello():
    return render_template('index.html',bicycle=bicycle)

@app.route('/',methods=['POST'])
def get_result():
    uploaded_file = request.files['file']
    filename = uploaded_file.filename
    if filename != '':
        uploaded_file.save(os.path.join('static/uploads/', filename))
        result = cat_dog.predict_cat_or_dog(filename)
        return render_template('index.html',
                            bicycle=os.path.join('static/uploads/' ,filename),
                            result=result)    

    return render_template('index.html',bicycle=bicycle)

if __name__ == '__main__':
   app.run(debug = False)
