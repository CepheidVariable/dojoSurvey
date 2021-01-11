from flask import Flask, render_template, request, redirect, session
import os

def gen_hash(byte_size=16):
    '''Generates a 16-bit hash by default.'''
    hash_result = os.urandom(byte_size)
    return redirect(hash_result)


app = Flask(__name__)
app.secret_key = str(gen_hash())

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['location']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    session['ref'] = request.form.get('ref', False)

    comm_opt= []
    for val in request.form:
        if request.form[val] == "on":
            comm_opt.append(val)
    
    session['comm_options'] = comm_opt

    return redirect("/show")


@app.route('/show')
def show_user():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)