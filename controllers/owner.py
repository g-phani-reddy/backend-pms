from flask_restx import Namespace, Resource, fields
from services import owner_services

owner_ns = Namespace('owner', description='Owner related operations')

owner_model = owner_ns.model('Owner', {
    'name': fields.String(required=True, description='The owner name'),
    'email': fields.String(required=True, description='Owner email'),
    'contact_no': fields.String(required=True, description='Contact No.'),
    'password': fields.String(required=True, description='password')
})


class Owner(Resource):

    @owner_ns.expect(owner_model)
    def post(self):
        try:
            paylod = owner_ns.payload
            name = paylod.get("name", "")
            email = paylod.get("email", "")
            contact_num = paylod.get("contact_no", "")
            password = paylod.get("password", "")

            #payload validation
            if len(name) == 0:
                return {"message": "Bad Request. Name should not be empty"}, 400
            
            elif len(email) == 0 or "@" not in email:
                return {"message": "Bad Request. Please provide valid email"}, 400

            elif len(contact_num) == 0:
                return {"message": 'Bad Request. Contact num should not be empty'}, 400
            
            elif len(password) == 0:
                return {"message": "Bad Request. Password cannot be empty"}, 400
            

            #create owner
            status, message = owner_services.create_owner(name, email, contact_num, password)

            if status:
                return {
                    "owner_id": str(message),
                    "message": "successfully created owner"
                    }, 201
            
            else:
                return {
                    "message": str(message)
                }, 400
        
        except Exception as e:
            print(str(e))
            return {
                "message": "Internal Server Error"
            }, 500


owner_ns.add_resource(Owner, "owner/signup")
