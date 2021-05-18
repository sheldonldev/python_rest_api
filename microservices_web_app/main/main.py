from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
from producer import publish


app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'

CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'product_id', 'user_product_unique')


@app.route('/api/products')
def products():
    return jsonify(Product.query.all())

@app.route('/api/products_users')
def products_users():
    return jsonify(ProductUser.query.all())

@app.route('/api/products/<int:id>/like')
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    user_id = req.json()['id']

    try:
        productUser= ProductUser(user_id=user_id, product_id=id)
        db.session.add(productUser)
        db.session.commit()
        publish("product_liked", id)
    except:
        abort(400, 'You already liked this product')


    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
