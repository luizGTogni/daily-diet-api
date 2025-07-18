from src import app
from src.models.meal import Meal
from flask import jsonify

@app.route("/meals", methods=["GET"])
def get_all():
    meals = Meal.query.all()

    return jsonify({ "meals": [meal.to_dict() for meal in meals], "total_meals": len(meals) })