from flask import Flask, render_template
from productos.rutas import productos_bp, productos
app = Flask(__name__)

app.register_blueprint(productos_bp)


@app.route("/item/<int:id>")
def detalle(id):
    for item in productos:
        if item["id"] == id:
            return render_template("detalle.html", producto = item)

if __name__ == "__main__":
    app.run(debug=True)