from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input as inceptionv3_preprocess_input
import re


app = Flask(__name__)


model = load_model("Projet_InceptionV3_model.h5")
model.make_predict_function()


map_dict = {0: 'Chenopodium (مزريطة)', 1: 'Cynodon (نجم)', 2: 'Malva (خبيز)', 3: 'Polypogon (ذيل الفار)'}

def predict_label(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = inceptionv3_preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed).argmax()
    prediction_score = model.predict(img_preprocessed)
    return map_dict[prediction], round(prediction_score[0][prediction] * 100, 2)

@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('home.html')

    
@app.route("/kashf", methods=['GET', 'POST'])
def kashf():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/cache/" + img.filename
        img.save(img_path)
        prediction, score = predict_label(img_path)  

        def convert_to_english(text):
            """
            لتحويل النص إلى حروف إنجليزية وحذف الحروف غير الإنجليزية.
            """
            # استخدام تعبير نظامي لاستخراج الحروف الإنجليزية فقط
            english_lowercase_letters = re.findall(r"[A-Za-z]", text)
            # دمج الحروف في سلسلة نصية واحدة
            return "".join(english_lowercase_letters)

        prediction_english = convert_to_english(prediction)
        return render_template('kashf.html', prediction = prediction, prediction_english = prediction_english, score = score, img_path = img_path)
    else :
        return render_template('kashf.html', title="Kashf")



@app.route("/chenopodium")
def chenopodium():
    return render_template('chenopodium.html', title="chenopodium")
@app.route("/cynodon")
def nejm():
    return render_template('cynodon.html', title="cynodon")
@app.route("/malva")
def malva():
    return render_template('malva.html', title="malva")
@app.route("/polypogon")
def polypogon():
    return render_template('polypogon.html', title="polypogon")

@app.route("/about")
def about():
        return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)