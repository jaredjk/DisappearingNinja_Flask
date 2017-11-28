from flask import Flask, render_template, request, redirect, session, flash, url_for
                                          
app = Flask(__name__)
app.secret_key = 'SecretKey'

                                          
@app.route('/')                                                                                 
def index():
    return render_template('index.html')  
@app.route('/ninja')                                                                                 
def ninja():
    mykey = True
    return render_template('ninja.html', mykey=mykey)  

@app.route('/ninja/<color>')                                                                                 
def each_ninja(color):
    mykey = False
    return render_template('ninja.html', color=color, mykey=mykey)    


app.run(debug=True)