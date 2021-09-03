from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/pred',methods=['GET','POST'])
def a():
    Process_temperature=request.form['Process_temperature']
    Rotational_speed=request.form['Rotational_speed']
    Torque=request.form['Torque']
    Tool_wear=request.form['Tool_wear']
    Machine_failure=request.form['Machine_failure']
    TWF=request.form['TWF']
    HDF=request.form['HDF']
    PWF=request.form['PWF']
    OSF=request.form['OSF']
    RNF=request.form['RNF']
    d={'Process_temperature':Process_temperature,'Rotational_speed':Rotational_speed,'Torque':Torque,'Tool_wear':Tool_wear,'Machine_failure':Machine_failure,
       'TWF':TWF,'HDF':HDF,'PWF':PWF,'OSF':OSF,'RNF':RNF}
    print(d)
    from ML import pred
    pred_value=pred(d)
    pred_value=float(pred_value)
    return render_template('result.html',result=pred_value)

@app.route('/back')
def back():
    return render_template('home_page.html')

if __name__=='__main__':
    app.run(debug=True)