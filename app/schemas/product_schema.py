from marshmallow import Schema, fields, validate


class ProductSchema(Schema):

    id = fields.Int(dump_only=True)

    supplier_ids = fields.Str(allow_none=True)

    product_code = fields.Str(
        allow_none=True,
        validate=validate.Length(max=25)
    )

    product_name = fields.Str(
        allow_none=True,
        validate=validate.Length(max=50)
    )

    description = fields.Str(allow_none=True)

    standard_cost = fields.Decimal(
        as_string=True,
        allow_none=True
    )

    list_price = fields.Decimal(
        as_string=True,
        required=True
    )

    reorder_level = fields.Int(allow_none=True)
    target_level = fields.Int(allow_none=True)

    quantity_per_unit = fields.Str(allow_none=True)

    discontinued = fields.Bool()

    minimum_reorder_quantity = fields.Int(allow_none=True)

    category = fields.Str(allow_none=True)