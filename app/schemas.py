from marshmallow import Schema, fields


class ToDoDetailSchema(Schema):
    id = fields.Int(load_only=True)
    name = fields.Str()
    slug = fields.Str()
    content = fields.Str()
    up_vote = fields.Int(load_only=True)
    down_vote = fields.Int(load_only=True)


class ToDoListSchema(Schema):
    id = fields.Int(load_only=True)
    name = fields.Str()
    up_vote = fields.Int()
    down_vote = fields.Int()


class VoteSchema(Schema):
    up = fields.Bool()
