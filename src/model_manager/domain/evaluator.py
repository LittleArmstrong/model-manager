

def calc_f1_score(precision:float, recall:float):
    try:
        result = 2 * (precision * recall) / (precision + recall) 
    except:
        result = 0
    return result