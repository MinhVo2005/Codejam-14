from ultralytics import YOLO



MINIMUM = 0.5

def get_class_and_conf(model, image_path, name_model):
    result = model(image_path, conf = MINIMUM)[0]
    boxes = result.boxes
    array  = []
    for box in boxes:
        conf = box.conf.cpu().numpy()[0]
        cls = box.cls.cpu().numpy()[0]
        classes = result.names[int(cls)]
        array.append((name_model, classes, conf))
    return array

 
def run_model():
    model1 = YOLO('')
    model2 = YOLO('')
    model3 = YOLO('')
    array1 = get_class_and_conf(model1, r"C:\GitHub\Codejam-14\images.jpg",'Vegetable')
    array2 = get_class_and_conf(model2, r'C:\GitHub\Codejam-14\images.jpg', 'Protein')
    array3 = get_class_and_conf(model3, r'C:\GitHub\Codejam-14\images.jpg', 'Grains')
    return array1 + array2 + array3
#Here is the main file
