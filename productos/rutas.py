from flask import Blueprint, render_template

productos_bp = Blueprint("productos", __name__, template_folder="templates")

productos = [
    {"id": 1, "nombre": "PlayStation 5 Slim", "precio": 509.90},
    {"id": 2, "nombre": "Xbox Series X", "precio": 449.95},
    {"id": 3, "nombre": "Razer Deathadder V3 Pro", "precio": 129.99},
    {"id": 4, "nombre": "Corsair Vengeance 16GB DDR5 4800 MHz", "precio": 98.95},
    {"id": 5, "nombre": "EA Sports FC 26", "precio": 44.99},
    {"id": 6, "nombre": "NBA 2K26", "precio": 19.99},
    {"id": 7, "nombre": "Nintendo Switch 2", "precio": 469.99},
    {"id": 8, "nombre": "Lenovo Ideapad Gaming 3", "precio": 779.99},
    {"id": 9, "nombre": "Call of Duty Black Ops 7", "precio": 79.99},
    {"id": 10, "nombre": "Logitech G29 Driving Force", "precio": 229.99}
    ]


@productos_bp.route("/")
def index():
    return render_template("index.html", productos = productos)