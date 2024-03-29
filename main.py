import random
import string
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/random_fact")
def random_fact():
    facts_list = ['Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.',
                  'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.', 
                  'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.', 
                  'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.']                                                       
    return f'<h3>{random.choice(facts_list)}</h3>'


@app.route("/password")
def password():
    symboles = ['123456789qwertyuiopasdfghjklzxcvbnm@#$%&']
    return f'<h2>Ваш сгенерированый пароль: {random.choice(symboles)}</h3>'


@app.route("/")
def index():
    return "<h1>Привет, посмотри факты <a href='/random_fact'>Посмотреть факты</a></h1> <p>Сгенерировать пароль <a href='/password'>посмотреть свой пароль</a><p> "


app.run(debug=True)
    return "<h1>Привет, здесь ты можешь получить свой надежный пароль: <a href='/password'>Забрать пароль</a></h1>"


app.run(debug=True)
