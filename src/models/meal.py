from src import db
from sqlalchemy import func

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    meal_date = db.Column(db.DateTime, nullable=False, default=func.now()) 
    is_diet = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "meal_date": self.meal_date,
            "is_diet": self.is_diet
        }