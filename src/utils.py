import os
import pickle
def save_obj(file_path: str, obj):
    os.makedirs(os.path.dirname(file_path), exist_ok= True)
    with open (file_path , 'wb') as f:
        return pickle.dump(obj, f)

def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)