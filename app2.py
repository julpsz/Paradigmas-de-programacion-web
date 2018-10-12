from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/", methods=["GET","POST"])
def index():
	return render_template("template3.html")
	if request.method == "POST":
		usuario=request.form["user"]
		clave=request.form["password"]
		if usuario=="julian":
			return render_template("template3.html")
		else:
			return render_template("template4.html")

@app.route("/hola")
def ingreso():
	return render_template("template1.html")
	


if __name__ == '__main__':
    app.run(debug=True)
