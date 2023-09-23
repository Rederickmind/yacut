from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                1,
                16,
                'Пользовательский вариант короткой ссылки не должен превышать 16 символов.'
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')