from datetime import datetime
import random

from flask import url_for

from yacut import db
from .constants import GENERATOR_ALPHABET, USER_INPUT_LIMIT


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'short_link_url', short_link_url=self.short, _external=True
            )
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])

    def get_unique_short_id(self):
        alphabet = GENERATOR_ALPHABET
        result_short_link = ''.join(random.choices(alphabet, k=6))
        return result_short_link

    def if_short_link_exists(self, short_link):
        return bool(self.query.filter_by(short=short_link).first())

    def is_valid_short_link(self, short_link):
        if len(short_link) > USER_INPUT_LIMIT:
            return False
        for value in short_link:
            if value not in GENERATOR_ALPHABET:
                return False
        return True