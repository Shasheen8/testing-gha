import pickle
def load_model(file):
    return pickle.load(file)  # A08: Insecure deserialization