class User:

    def __init__(self, id=None, uuid=None, first_name=None, last_name=None, email=None, phone_number=None, role=None,
                 organization=None, authentication_token=None, created_at=None, updated_at=None):
        self.id = id
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone_number
        self.role = role
        self.org = organization
        self.auth_token = authentication_token
        self.created = created_at
        self.updated = updated_at
