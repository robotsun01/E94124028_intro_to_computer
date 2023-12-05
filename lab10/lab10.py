import random

from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('lab10.html')


@app.route('/student_data', methods = ['POST'])
def root():
    Name = request.form['Name'] #take out "Name" data
    ID = request.form['ID'] #take out "ID" data
    print("name : ", Name)
    print("Student_id : ", ID)
    return "ok"

@app.route('/rsp', methods = ['GET'])
def mora():
    abc = request.args['choice'] #take out "choice" data
    ABC = random.choice(['s','r','p']) #radomly take data on [s r p]
    try:
        print("computer : ", ABC , " ", "user : ", abc)
        if abc == ABC : #mora law
            return "It's Tie"
        elif (abc == "s" and ABC == "r") or (abc == "r" and ABC == "p") or (abc == "p" and ABC == "s"):
            return "You Lose!"
        elif (abc == "s" and ABC == "p") or (abc == "r" and ABC == "c") or (abc == "p" and ABC == "r"):
            return "You Win!"
        else:
            return "輸入有誤，請重新輸入"
    except:
        pass




app.run(host= "0.0.0.0" ,port =3000, debug=True)