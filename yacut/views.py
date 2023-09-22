import random
import string

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    alphabet = (
        string.ascii_lowercase + string.ascii_uppercase + string.digits
    )
    return ''.join(random.choices(alphabet, k=16))