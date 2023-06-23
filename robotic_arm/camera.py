from tasks.object_detection import ObjectDetection

class Camera:
    def __init__(self):
        self.object_detection = ObjectDetection()

    def detect_object(self, image):
        # Use the object detection model to detect objects in the image
        detected_objects = self.object_detection.detect_object(image)
        return detected_objects
