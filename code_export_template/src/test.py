from ultralytics import YOLO

# lokales Modell laden
model = YOLO("custom_yolov12n.pt") 

# Modell testen
# Dokumentation: https://docs.ultralytics.com/de/modes/val/#key-features-of-val-mode
metrics = model.val(
    data= "dataset/data.yaml",
    batch= 16,
    save_json= True, # Vorhersagen extra speichern
    plots= True,
    split= "test", # Bilder aus dem Datensatz zum testen
    project= "runs/testing", # Speicherort
    name= "test1",
    verbose= True,
    save_txt= True,
    save_conf= True,
    visualize = True,
    exist_ok = True,
)  
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  #  mAP50-95 für jede Klasse
metrics.to_df().rows(named=True) # alle Metriken für alle Klassen
metrics.results_dict # Gesamtmetrik

# Vorhersagen sind im Speicherort unter predictions.json