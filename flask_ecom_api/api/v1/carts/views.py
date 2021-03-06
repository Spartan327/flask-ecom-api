from http import HTTPStatus

from flask import Blueprint, abort, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Cart, CartProduct  # type: ignore
from flask_ecom_api.api.v1.carts.schemas import cart_product_schema, cart_schema
from flask_ecom_api.api.v1.common.responses import ApiSuccess
from flask_ecom_api.app import db

cart_blueprint = Blueprint('carts', __name__, url_prefix='/api/v1')


@cart_blueprint.route('/carts', methods=['POST'])
@use_args(cart_schema)
@jwt_required()
def create_cart(args):
    """Create new cart."""
    new_cart = Cart(
        reference=args.get('reference'),
    )
    db.session.add(new_cart)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiSuccess(
        schema=cart_schema,
        response_db_query=new_cart,
        status=HTTPStatus.CREATED,
    ).response()


@cart_blueprint.route('/carts/items', methods=['POST'])
@use_args(cart_product_schema)
@jwt_required()
def add_product_to_cart(args):
    """Add product to cart."""
    new_cart_product = CartProduct(
        cart_id=args.get('cart_id'),
        restaurant_product_id=args.get('restaurant_product_id'),
        quantity=args.get('quantity'),
    )
    db.session.add(new_cart_product)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiSuccess(
        schema=cart_product_schema,
        response_db_query=new_cart_product,
        status=HTTPStatus.CREATED,
    ).response()


@cart_blueprint.route('/carts/<string:cart_reference>', methods=['GET'])
@jwt_required()
def cart_detail(cart_reference):
    """Get cart detail."""
    try:
        cart = Cart.query.filter_by(reference=cart_reference).first()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return jsonify(
        {
            'data': cart_schema.dump(cart),
            'total_amount': cart.total_amount(),
        },
    ), HTTPStatus.OK
