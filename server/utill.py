import json
import pickle
import numpy as np 

__location = None
__columns = None
__model = None

def get_price(loc,sqft,bath,bhk):
    load_artifacts()
    try:
        loc_index = __columns.index(loc.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    load_artifacts()
    return __location

def load_artifacts():
    print("loading artifacts")
    global __location
    global __columns
    global __model

    with open("./server/artifacts/columns.json","r") as f:
        __columns = json.load(f)['data_columns']
        __location = __columns[3:]
    with open("./server/artifacts/banglore_home_prices_model.pickle","rb") as f:
        __model = pickle.load(f)
    print("loaded")

if __name__ == "__main__":
    load_artifacts()
    print(get_location_names())
    print(get_price('1st Phase JP Nagar',1500, 2, 2))