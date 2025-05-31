import pickle

def load_data():
    with open('data.pkl', 'rb') as f:
        return pickle.load(f)