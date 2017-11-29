class Location:

    def __init__(self, id=None, display_name=None, created_at=None, updated_at=None, sensor_ids=None,
                 links=None, sensors=None):
        self.id = id
        self.display_name = display_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.sensor_ids = sensor_ids
        self.sensors = sensors
        self.links = links
