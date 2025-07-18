from datetime import timezone, datetime
from src import app, db
from src.models.meal import Meal
from flask import request, jsonify

@app.route("/meals", methods=["POST"])
def create():
    name, description, meal_date, is_diet = request.get_json().values()
    
    if not (name and description and meal_date and is_diet):
        return jsonify({ "error": "Credentials is missing or invalid" }), 400
    
    meal_date_datetime = datetime.strptime(meal_date, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    meal_date_already_exists = Meal.query.filter_by(meal_date=meal_date_datetime).first()

    if meal_date_already_exists:
        return jsonify({ "error": "There is already a meal registered for that date and time" }), 409
        
    meal = Meal(name=name, description=description, meal_date=meal_date_datetime, is_diet=is_diet)
    db.session.add(meal)
    db.session.commit()
    
    return jsonify(meal.to_dict())

    