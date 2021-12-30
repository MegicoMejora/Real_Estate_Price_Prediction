from flask.json import jsonify


import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading the saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/Bangalore_house_price_prediction.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("Loading the saved artifacts...done")
        


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names()) 
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 3))  
    print(get_estimated_price('Rajaji Nagar', 1549, 2, 2)) 
    