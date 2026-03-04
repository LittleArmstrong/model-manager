from ultralytics import YOLO

# model = YOLO("yolov12n.pt") # pretrained modell runterladem
# model = YOLO("yolov12n.yaml") # modell ohne Gewichtsparameter laden
model = YOLO("custom_yolov12n.pt") # lokales Modell laden

# Doku unter https://docs.ultralytics.com/de/modes/train/#resuming-interrupted-trainings für alle Argumente
yolo_results = model.train(
        data="dataset/data.yaml",
        imgsz=640,
        batch=16,
        epochs=10,
        lr0= 0.01, # initiale Lernrate
        freeze= 0, # transfer learning
        optimizer = "auto", # Adam, AdamW, SGD
        weight_decay =0.0005,
        project="runs/training",
        name="train1",
        verbose=True,
        exist_ok =True, # ob vorheriges Training überschrieben werden soll
        plots=True
    )
# Modell wird in runs/training gespeichert, also runs/training/train1
