class ExercisePlan:
    id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        hours_to_min = hours * 60
        return cls(trainer_id, equipment_id, hours_to_min)

    @staticmethod
    def get_next_id():
        next_id = ExercisePlan.id
        ExercisePlan.id += 1
        return next_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
