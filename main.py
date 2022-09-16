from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

# db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
     })

@app.route("/all")
def all_cafes():
    cafe_list = []
    cafes = db.session.query(Cafe).all()
    for cafe in cafes:
        cafe_item = {
        "id": cafe_item.id,
        "name": cafe_item.name,
        "map_url": cafe_item.map_url,
        "img_url": cafe_item.img_url,
        "location": cafe_item.location,
        "seats": cafe_item.seats,
        "has_toilet": cafe_item.has_toilet,
        "has_wifi": cafe_item.has_wifi,
        "has_sockets": cafe_item.has_sockets,
        "can_take_calls": cafe_item.can_take_calls,
        "coffee_price": cafe_item.coffee_price,
     }
        cafe_list.append(cafe_item)
    return jsonify(cafes=cafe_list)


#TODO HTTP POST - Create

#TODO HTTP PUT/PATCH - Update

#TODO HTTP DELETE - Delete


if __name__ == '__main__':
    app.run(debug=True)
