from src import app
from src.models.meal import Meal
from flask import jsonify

@app.route("/meals/<int:meal_id>", methods=["GET"])
def get_one(meal_id):
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({ "error": "Meal not found" }), 404

    return jsonify(meal.to_dict())