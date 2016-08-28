from . import db, ma


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assembly_id = db.Column(db.Integer)
    name = db.Column(db.String(120))
    status = db.Column(db.String(30))
    sponser = db.Column(db.String(50))
    proposed_date = db.Column(db.DateTime)
    decision_date = db.Column(db.DateTime)
    is_processed = db.Boolean()

    def __repr__(self):
        return self.name


class BillListSchema(ma.ModelSchema):
    class Meta:
        model = Bill


bill_list_schema = BillListSchema(many=True)
