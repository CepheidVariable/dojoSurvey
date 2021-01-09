from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    first_name_from_form= request.form['first_name']
    last_name_from_form= request.form['last_name']
    location_from_form= request.form.get('location', False)
    fav_lang_from_form= request.form['fav_lang']
    comments_from_form= request.form['comments']
    ref_from_form= request.form.get('ref', False)
    
    comm_opt= []
    for val in request.form:
        if request.form[val] == "on":
            comm_opt.append(val)
    
    return render_template("show.html", first_name_on_template= first_name_from_form, last_name_on_template= last_name_from_form, location_on_template= location_from_form, fav_lang_on_template= fav_lang_from_form, comments_on_template= comments_from_form, ref_on_template= ref_from_form, comm_opt= comm_opt)


if __name__ == "__main__":
    app.run(debug=True)