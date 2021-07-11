from flask import Flask, request, render_template
import base64
from PIL import Image
import io
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)

CLASS_NAMES = ["circle", "square", "triangle"]
IMG_SHAPE = (64, 64)
model = load_model("trained_models/model.h5")

def get_class(predictions):
    return CLASS_NAMES[predictions.argmax()]

def decode_image(img_data):
    # Parse the base64 part of the string
    img_data = re.sub('^data:image/.+;base64,','',img_data)

    # BUG_FIX : convert all ' ' to '+' 
    img_data = img_data.replace(' ','+')

    # Decode the image
    image = Image.open(io.BytesIO(base64.b64decode(img_data)))

    return image

def preprocess_image(image):
    # Resize the image to shape
    image = image.resize(IMG_SHAPE).convert('L')

    # Convert the image to an array to feed into the model
    img_arr = img_to_array(image) / 255.0
    img_arr = img_arr.reshape([1] + list(img_arr.shape))

    return img_arr



@app.route('/')
def index():
    return render_template("game.html")


@app.route("/predict", methods=['POST'])
def predict():
    # Get the image data from request
    img_data = request.form['imgData']

    # Decode the image
    image = decode_image(img_data)

    # Preprocess image
    img_arr = preprocess_image(image)

    # Predict the target class
    predictions = model.predict(img_arr)
    shape_name = get_class(predictions)
    
    return shape_name

if __name__ == '__main__':
    app.run(debug=True)    