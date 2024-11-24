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
        array.append((classes,name_model, conf))
    return array

 
def run_model(image):
    model1 = YOLO(r'best_vegetable.pt')
    model2 = YOLO(r'best_meat.pt')
    model3 = YOLO(r'best_whole_grain.pt')
    array1 = get_class_and_conf(model1, image,'Vegetable')
    array2 = get_class_and_conf(model2, image, 'Protein')
    array3 = get_class_and_conf(model3, image, 'Grains')
    return array1 + array2 + array3

#Here is the main file

def store_data(sample):
    filename = 'results.json'
    
    # Create a new instance of Calculations
    cal = cl.Calculations()
    
    # Load existing results from the JSON file or initialize empty dictionaries
    cal.load_results(filename)

    # Classify the new groupings
    cal.classify(sample)

    # Save the updated results back to the JSON file
    cal.save_results(filename)


