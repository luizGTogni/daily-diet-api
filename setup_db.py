from src import db, app

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database Created")