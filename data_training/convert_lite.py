import tensorflow as tf
import os

converter = tf.lite.TFLiteConverter.from_saved_model(os.getcwd())
tflite_model = converter.convert()

open("converted_model.tflite","wb").write(tflite_model)
