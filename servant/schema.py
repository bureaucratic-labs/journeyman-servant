"""All JSON schemas used at project."""

from marshmallow import Schema, fields


class RequestSchema(Schema):
    """Request JSON schema."""

    items = fields.List(fields.String, description='Array of strings to be processed', many=True, example=['1 к кв', 'двушка', 'трёхкомнатная квартира'])


class ResponseSchema(Schema):
    """Response JSON schema."""

    items = fields.List(fields.String, description='Array of result labels', example=['1', '2', '3'])
