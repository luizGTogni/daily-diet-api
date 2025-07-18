from datetime import timezone, datetime
from src import app, db
from src.models.meal import Meal
from flask import request, jsonify

@app.route("/meals/<int:meal_id>", methods=["PUT"])
def update(meal_id):
    name, description, meal_date, is_diet = request.get_json().values()
    
    if not (name and description and meal_date):
        return jsonify({ "error": "Credentials is missing or invalid" }), 400
    
    meal_current = Meal.query.get(meal_id)

    if not meal_current:
        return jsonify({ "error": "Meal not found" }), 404

    meal_date_datetime = datetime.strptime(meal_date, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    meal_date_already_exists = Meal.query.filter_by(meal_date=meal_date_datetime).first()

    if meal_date_already_exists and meal_date_already_exists.id != meal_id:
        return jsonify({ "error": "There is already a meal registered for that date and time" }), 409

    meal_current.name = name
    meal_current.description = description
    meal_current.meal_date = meal_date_datetime
    meal_current.is_diet = is_diet
    db.session.commit()
    
    return jsonify(meal_current.to_dict())

    