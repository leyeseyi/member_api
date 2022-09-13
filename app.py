from flask import Flask, g, request
from database import get_db

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/members', methods=['GET'])
def get_members():
    new_member_data =request.get_json()
    
    name = new_member_data['name']
    email = new_member_data['email']
    level = new_member_data['level']
    
    db = get_db()

    db.execute('insert into members (name, email, level) values (?,?,?)',[name, email, level])
    db.commit()
    return 'The name is {}, email is {}, level is {}'.format(name,email, level)

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    return 'This returns one member by ID'

@app.route('/members', methods=['POST'])
def add_member():

    return 'This adds a new member.'

@app.route('/members/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return 'This updates a member by ID.'

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'This removes a member by ID.'

if __name__ == '__main__':
    app.run(debug=True)