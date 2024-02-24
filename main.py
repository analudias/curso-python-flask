from comunidadeimpressionadora import app, database

with app.app_context():
    database.drop_all()
    database.create_all()

if __name__ == '__main__':
    app.run(debug=True)