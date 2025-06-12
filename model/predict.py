import pickle
import pandas as pd

# import the ml model
with open('./model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
 # comes from mlflow version registry    
MODEL_VERSION = '1.0.0'
   
 # get class labels from model 
class_labels = model.classes_.tolist()   
    
def predict_output(user_input: dict):
    input_df = pd.DataFrame(user_input, index=[0])
    
    #predict the class
    predicted_class = model.predict(input_df)[0]
    
    #get the probability for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    
    #create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))
    
    return {
        "predicted_category" : predicted_class,
        "confidence" : round(confidence,4),
        "class_probabilities" : class_probs
    }
    
    
    # prediction = model.predict(input_df)[0]   
    # return prediction 