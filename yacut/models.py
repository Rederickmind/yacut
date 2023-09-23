from datetime import datetime
import random

from yacut import db
from .constants import GENERATOR_ALPHABET


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])

    def get_unique_short_id():
        alphabet = GENERATOR_ALPHABET
        return ''.join(random.choices(alphabet, k=16))

    def if_short_link_exists(self, short_link):
        return bool(self.query.filter_by(short=short_link).first())