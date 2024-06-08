from flask import Flask, request, url_for, render_template
import sqlite3 
app = Flask(__name__)

connect = sqlite3.connect('mydb.db')
connect.execute('CREATE TABLE IF NOT EXISTS user (name TEXT, email TEXT, password TEXT)')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name =  request.form['username']
        email =  request.form['email']
        password =  request.form['password']    
        connect = sqlite3.connect('mydb.db')
        connect.execute('INSERT INTO user (name,email,password) VALUES (?,?,?)', (name, email, password))
        connect.commit()
        return render_template('login.html')
    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password'] 
        connect = sqlite3.connect('mydb.db')
        users = connect.execute('SELECT * FROM user WHERE name = ?', [name])
        user1 = users.fetchone()
        print("------------------------------------")
        print(user1)
        if user1:
            name1 = user1[0]
            user11 = user1[2]
            if user11 == password:
                return render_template('home.html', name1=name1)
            else:
                errormsg = "Invalid Password!"
                return render_template('login.html', errormsg=errormsg)
              
        else:
            errormsg = "Invalid Username!"
            return render_template('login.html', errormsg=errormsg)
    else:

      return render_template('login.html')

@app.route('/login/tools')
def tools():
    return render_template('tools.html')

    
if __name__ == '__main__':
    app.run(debug=True)