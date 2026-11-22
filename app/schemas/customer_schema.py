from marshmallow import Schema, fields, validate


class CustomerSchema(Schema):

    id = fields.Int(dump_only=True)

    company = fields.Str(
        allow_none=True,
        validate=validate.Length(max=50)
    )

    first_name = fields.Str(
        allow_none=True,
        validate=validate.Length(max=50)
    )

    last_name = fields.Str(
        allow_none=True,
        validate=validate.Length(max=50)
    )

    email_address = fields.Email(
        allow_none=True,
        validate=validate.Length(max=50)
    )

    job_title = fields.Str(allow_none=True)

    business_phone = fields.Str(allow_none=True)
    home_phone = fields.Str(allow_none=True)
    mobile_phone = fields.Str(allow_none=True)
    fax_number = fields.Str(allow_none=True)

    address = fields.Str(allow_none=True)
    city = fields.Str(allow_none=True)
    state_province = fields.Str(allow_none=True)
    zip_postal_code = fields.Str(allow_none=True)
    country_region = fields.Str(allow_none=True)

    web_page = fields.Str(allow_none=True)
    notes = fields.Str(allow_none=True)