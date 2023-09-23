from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_short_link = form.custom_id
        url_map = URLMap()

        if not custom_short_link:
            custom_short_link = url_map.get_unique_short_id()

        if URLMap.if_short_link_exists():
            flash(
                'Ваш вариант короткой ссылки уже занят!'
            )
            return render_template('index.html', form=form)
        short_link = URLMap(
            original=form.original_link.data,
            short=custom_short_link
        )
        db.session.add(short_link)
        db.session.commit()
        flash(
            url_for(
                'short_link_url',
                short_link_url=custom_short_link,
                _external=True
            )
        )
        return render_template('index.html', form=form)


@app.route('/<string:short_link_url>', methods=('GET',))
def short_link_url(short_link_url):
    url_map = URLMap.query.filter_by(short=short_link_url).first()
    if not url_map:
        abort(404)
    return redirect(url_map.original)
