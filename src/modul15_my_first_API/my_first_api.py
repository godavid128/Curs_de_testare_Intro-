'''
Diferenta dintre 'url params' si 'body params'?
-url params - ex: name=ion; - se adauga o extensie la url ns cu parametri
-body params -nu sunt vizibil in url, ci ii ai ca si post request, ii atasezi tu
'''

from flask import Flask, jsonify, request

# Flask - clasa de baza, pe care o instantiem pt a crea propriul API
# jsonify - converteste inform. din jsonify in niste date pe care server le poate interpreta

server_port = 8000
app = Flask(__name__)
app.config['DEBUG'] = True
users = [
    {'name': 'John',
     'email': 'a@gmail.com',
     'salary': 30000}
]


# Cum trasmitem datele astea printr-un server la client. Ce treb sa creem? o functie
@app.route('/')  # o route - e calea catre diferite puncte finale
def get_all_users():
    return users


@app.route('/users')
def get_users():
    return jsonify({'users': users})


@app.route('/blog')
def get_blogul_meu():
    return '<p>Hello world<p>'


@app.route('/users', methods=['POST'])
def post_user():
    usr = request.get_json()
    for u in users:
        if usr['email'] == u['email']:
            return f'{usr["email"]} already taken', 200
    else:
        users.append(usr)
        return 'user added', 201


if __name__ == '__main__':
    app.run('localhost', port=server_port, debug=True)
