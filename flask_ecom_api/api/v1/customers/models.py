from sqlalchemy_utils import EmailType, PhoneNumberType

from flask_ecom_api.api.v1.customers.admin import (
    CustomerAdminView,
    CustomerShippingAddressAdminView,
)
from flask_ecom_api.api.v1.orders.models import Order
from flask_ecom_api.app import admin, db


class Customer(db.Model):
    """Customer model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=50),
        index=True,
        unique=True,
        nullable=False,
    )
    date_of_birth = db.Column(db.DateTime)
    email = db.Column(
        EmailType,
        index=True,
        unique=True,
        nullable=False,
    )

    shipping_addresses = db.relationship(
        'CustomerShippingAddress',
        backref='customer',
        lazy='joined',
    )
    orders = db.relationship(Order, lazy='joined')

    def __repr__(self):
        """Printable representation of Customer model."""
        return f'<Customer id: {self.id}, customer name: {self.name}>'


class CustomerShippingAddress(db.Model):
    """Customer shipping address model."""

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customer.id'),
        index=True,
        nullable=False,
    )
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(PhoneNumberType())
    country = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(140))

    customers = db.relationship('Customer', lazy='joined')

    def __repr__(self):
        """Printable representation of CustomerShippingAddress model."""
        return f'<Customer shipping address id: {self.id}>'


admin.add_view(
    CustomerAdminView(
        Customer,
        db.session,
        category='Customers',
    ),
)

admin.add_view(
    CustomerShippingAddressAdminView(
        CustomerShippingAddress,
        db.session,
        category='Customers',
    ),
)
