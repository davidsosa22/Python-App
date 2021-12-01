from marshmallow import Schema, fields
#create schema for githubrepo
class GithubRepoSchema(Schema):
  id = fields.Int(required=True)
  repo_name = fields.Str()
  full_name = fields.Str()
  language = fields.Str()
  description = fields.Str()
  repo_url = fields.URL()

#create kudo schema
class KudoSchema(GithubRepoSchema):
  user_id = fields.Email(required=True)