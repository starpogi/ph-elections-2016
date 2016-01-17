from flask import Flask
from flask import render_template
import views

app = Flask(__name__)
app.register_blueprint(views.base_app)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
