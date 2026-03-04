from ultralytics import YOLO

# lokales Modell laden
model = YOLO("custom_yolov12n.pt") 

# Vorhersagen Pfad zu einem Bild oder einer Liste:
results = model(["dataset/images/test/000000000042.jpg", "dataset/images/test/000000000049.jpg"]) 

# Process results list
for result in results:
    boxes = result.boxes  # Bounding Boxes
    result.show()  # zeigen
    result.save(filename="result.jpg")  # speichern 