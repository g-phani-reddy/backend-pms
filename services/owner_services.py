from models.owner import Owner
import uuid

def create_owner(name, email, contact_no, password):
    try:
        owner_id = str(uuid.uuid4())
        owner_instance = Owner(owner_id=owner_id, 
                               name=name, email=email, contact_num = contact_no, password =password)
        owner_instance.save()
        return True, owner_id

    except Exception as e:
        print(str(e))
        return False, None

