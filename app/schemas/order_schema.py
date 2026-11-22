from marshmallow import Schema, fields, validate


class OrderSchema(Schema):

    id = fields.Int(dump_only=True)

    employee_id = fields.Int(allow_none=True)
    customer_id = fields.Int(required=True)

    order_date = fields.DateTime(allow_none=True)
    shipped_date = fields.DateTime(allow_none=True)

    shipper_id = fields.Int(allow_none=True)

    ship_name = fields.Str(allow_none=True)
    ship_address = fields.Str(allow_none=True)
    ship_city = fields.Str(allow_none=True)
    ship_state_province = fields.Str(allow_none=True)
    ship_zip_postal_code = fields.Str(allow_none=True)
    ship_country_region = fields.Str(allow_none=True)

    shipping_fee = fields.Decimal(as_string=True, allow_none=True)
    taxes = fields.Decimal(as_string=True, allow_none=True)

    payment_type = fields.Str(allow_none=True)
    paid_date = fields.DateTime(allow_none=True)

    notes = fields.Str(allow_none=True)
    tax_rate = fields.Float(allow_none=True)
    tax_status_id = fields.Int(allow_none=True)
    status_id = fields.Int(allow_none=True)
