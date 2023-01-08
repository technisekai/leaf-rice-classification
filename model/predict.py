import tensorflow as tf
from PIL import Image
import keras.utils as image
import numpy as np
import json

PATH_MODEL = 'model/NF_batch_size4_D0.2_save.h5'
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
  # json data descriptions of disease
  with open('model/descriptions.json', 'r', encoding='utf-8') as f:
    DESC = json.load(f)
  
  test_image = input_img(img_path)

  # result class and score
  predict = MODEL.predict(test_image)
  class_test_img = CLASS_DATA[np.argmax(predict)]
  score_test_img = np.max(predict)

  if class_test_img == 'Sehat' and score_test_img < 0.5:
    print('runn')
    all_score = np.argsort(predict)[0]
    DESC["desc"][1]["explain"] = "Daun padi terdeteksi sehat namun dengan score kepercayaan yang rendah. Ada kemungkinan padi mengidap penyakit."
    DESC["desc"][1]["solution"] = [CLASS_DATA[all_score[i]]+": "+str(predict[0][all_score[i]]) for i in reversed(range(3))]
  
  return {
    "path_img": img_path,
    "class": class_test_img,
    "score": score_test_img, 
    "desc": DESC['desc'][np.argmax(predict)]
  }