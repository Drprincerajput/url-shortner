from .extensions import db
import string
from random import choices


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(6), unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generator_short_url()

    def generator_short_url(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))

        url = self.query.filter_by(short_url=short_url).first()
        if url:
            return self.generator_short_url()
        return short_url
