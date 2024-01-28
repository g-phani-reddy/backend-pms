from run import db
import datetime

class Owner(db.Document):
    owner_id = db.StringField(max_length=50)
    name = db.StringField(max_length=60)
    contact_num = db.StringField(max_length=15)
    email = db.StringField(max_length=50, unique=True)
    password = db.StringField()
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return {
            "owner_id": str(self.owner_id),
            "name": str(self.name),
            "contact_num": str(self.contact_num),
            "email": str(self.email),
            "created_at": str(self.created_at)
        }
