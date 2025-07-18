from src import app, db
from src.models.meal import Meal
from flask import jsonify

@app.route("/meals/<int:meal_id>", methods=["DELETE"])
def delete(meal_id):
    meal_current = Meal.query.get(meal_id)

    if not meal_current:
        return jsonify({ "error": "Meal not found" }), 404

    db.session.delete(meal_current)
    db.session.commit()
    
    return jsonify({ "message": "Meal deleted successfully", "meal_id": meal_id })

    