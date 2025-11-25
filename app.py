from flask import Flask, render_template
from productos.rutas import productos_bp
app = Flask(__name__)

app.register_blueprint(productos_bp)


if __name__ == "__main__":
    app.run(debug=True)