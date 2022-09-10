import pickle
import datetime

def serialize(ml_model):
    """
    Converts a model to a pickle object and saves it to local file storage
    """
    # get current date and current time - UTC
    current_time = datetime.datetime.now()
    # Save the trained model as a pickle string.
    fileName = current_time.strftime("%d-%m-%Y-%H:%M:%S:%f")+'.pkl'
    # saves to my current directory
    # Optional: change directory using os.chdir(my_path)
    with open(fileName, 'wb') as f:
        pickle.dump(ml_model, f)
    
def deserialize(filePath):
    """
    Opens a pickle file and accesses the pickle object
    """
    with open(filePath, 'rb') as f:
        model_from_pickle = pickle.load(f)
        return model_from_pickle