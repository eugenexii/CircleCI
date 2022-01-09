from flask import Flask, render_template
app=Flask(__name__)
app.config['SECRET_KEY'] = "lkrt53qxcr612303oe4vperrejkb5"
@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5656
    )