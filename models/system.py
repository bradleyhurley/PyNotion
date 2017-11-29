class System:

    def __init__(self, id=None, uuid=None, name=None, mode=None, latitude=None, longitude=None, timezone_id=None,
                 locality=None, postal_code=None, administrative_area=None,  fire_number=None, police_number=None,
                 emergency_number=None, night_time_start=None, night_time_end=None, created_at=None, updated_at=None,
                 links=None):
        self.id = id
        self.uuid = uuid
        self.name = name
        self.mode = mode
        self.latitude = latitude
        self.longitude = longitude
        self.timezone_id = timezone_id
        self.locality = locality
        self.postal_code = postal_code
        self.administrative_area = administrative_area
        self.fire_number = fire_number
        self.police_number = police_number
        self.emergency_number = emergency_number
        self.night_time_start = night_time_start
        self.night_time_end = night_time_end
        self.created_at = created_at
        self.updated_at = updated_at
        self.links = links
