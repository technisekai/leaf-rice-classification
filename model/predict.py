import tensorflow as tf
import keras.utils as image
import numpy as np

PATH_MODEL = 'model_efficientb3_agro73.h5'
CLASS_DATA = ['Bercak Coklat', 'Sehat', 'Hispa', 'Blas'] # warning this is not fixed yet
MODEL = tf.keras.models.load_model(PATH_MODEL)

# conv image to numeric
def input_img(path):
  img = image.load_img(path, target_size=(300, 300))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  return images

# predict
def predict(img_path):
    input_img = input_img(img_path)
    predict = MODEL.predict(input_img('/content/IMG_20190419_094756.jpg'))
    return CLASS_DATA[np.argmax(predict)], np.max(predict)