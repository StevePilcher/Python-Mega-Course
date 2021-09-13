from flask import Flask, render_template

app = Flask(__name__)

# Templates must be saved in a templates directory


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
