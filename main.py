from ultralytics import YOLO
import cv2
import classification as cl



MINIMUM = 0.5
def get_class_and_conf(model, image_path, name_model):
    result = model.predict(image_path, conf = MINIMUM)[0]
    boxes = result.boxes
    array  = []
    for box in boxes:
        conf = box.conf.cpu().numpy()[0]
        cls = box.cls.cpu().numpy()[0]
        classes = result.names[int(cls)]
        if name_model == 'Protein':
            classes = "Meat"
        array.append((classes,name_model, conf))
    return array

 
def run_model(image):
    model1 = YOLO(r'models/best_vegetable.pt')
    model2 = YOLO(r'models/best_meat.pt')
    model3 = YOLO(r'models/best_whole_grain.pt')
    array1 = get_class_and_conf(model1, image,'Vegetable')
    array2 = get_class_and_conf(model2, image, 'Protein')
    array3 = get_class_and_conf(model3, image, 'Grains')
    return array1 + array2 + array3

#Here is the main file




