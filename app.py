from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
model = pickle.load(open("logit.pkl", 'rb'))  # read mode
app = Flask(__name__)  # initializing Flask app

@app.route("/",methods=['GET', 'POST'])
# def hello():
#     return render_template('index.html')

#details of index.html through the below code snippet
@app.route("/predict", methods=['POST','GET'])
def predict():
    result = 0
    if request.method == 'POST':
       CLMINSUR = int(request.form['CLMINSUR'])
       SEATBELT = int(request.form['SEATBELT'])
       CLMAGE = int(request.form['CLMAGE'])
       CLMSEX = int(request.form['CLMSEX'])
       LOSS = float(request.form['LOSS'])
       list1 = [CLMAGE,LOSS,CLMINSUR,CLMSEX,SEATBELT]
       print(list1)
       data = pd.DataFrame({'CLMAGE':[CLMAGE],'LOSS':[LOSS],'CLMINSUR':[CLMINSUR],'CLMSEX':[CLMSEX],'SEATBELT':[SEATBELT]})
       #int_features = [x for x in list1]
       #features = [np.array(int_features)]
       #print(features)
       prediction= model.predict(data)
       print(prediction[0])
       
       if prediction[0] > 0.5:
           result = 1
       else:
           result = 0
       #type(prediction)
       return render_template('index.html', prediction_text = 'Presence of Attorney or Not {}'.format(result))
       
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()


