#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask, request,jsonify,render_template
import pickle
import numpy as np
import math





app=Flask(__name__)
model=pickle.load(open('salary.pkl','rb'))



@app.route('/')
def home():   
    return render_template("jack.html")
@app.route('/predict',methods=["GET","Post"])
def predict():
    int_features  = [int (x) for x in request.form.values()]
    int_features=[int_features]
    print(int_features)
    predicition=model.predict(int_features)
    output=round(predicition[0])
    return render_template('jack.html',prediction_text=output)
if __name__ == '__main__':
    app.run()


# In[1]:





# In[ ]:




