import tensorflow as tf
import numpy as np

class ObjectDetection:
    def __init__(self):
        # Load the pre-trained model
        self.model = tf.keras.applications.MobileNetV2(weights='imagenet')
        self.input_shape = self.model.input_shape[1:3]

    def preprocess_image(self, image):
        # Preprocess the input image
        image = tf.image.resize(image, self.input_shape)
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
        return image

    def postprocess_predictions(self, predictions):
        # Postprocess the model predictions
        class_names = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]
        detected_objects = [
            {
                'class': class_name,
                'score': float(score),
                'bounding_box': (ymin, xmin, ymax, xmax)
            }
            for _, class_name, score, (ymin, xmin, ymax, xmax) in class_names
        ]
        return detected_objects

    def detect_object(self, image):
        # Preprocess the input image
        preprocessed_image = self.preprocess_image(image)

        # Run the object detection model
        predictions = self.model.predict(np.expand_dims(preprocessed_image, axis=0))

        # Postprocess the predictions
        detected_objects = self.postprocess_predictions(predictions)

        return detected_objects
