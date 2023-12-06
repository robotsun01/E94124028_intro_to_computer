import json
from flask import *
app = Flask(__name__)

String2 = {}

@app.route('/', methods=['GET'])
def index():
    return render_template('lab10_plus.html')


@app.route('/set', methods=['POST'])
def root():
    ret = request.form.get('store_name') #take data from html
    Score = request.form.get('score')
    String1 = {'store_name' : ret, 'score': Score}
    String2[ret] = Score
    print("user input data : ", String1)
    print("Data on server : ", String2)
    String3 = json.dumps(String2,ensure_ascii = False) # change data into json
    return render_template('lab10_plus.html', **locals()) # let data save to lab10_plus.html

@app.route('/reset/<choice>', methods=['GET'])
def reset(choice):
    if choice == "y" :
        String2.clear()
        return render_template('reset.html') # reset 
    else:
        return render_template('lab10_plus.html') # back to the main page



app.run(host= "0.0.0.0" ,port =3000, debug=True)