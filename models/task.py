class Task:

    def __init__(self, id=None, task_type=None, sensor_data=None, status=None,
                 created_at=None, updated_at=None, sensor_id=None, links=None):
        self.id = id
        self.task_type = task_type
        self.sensor_data = sensor_data
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.sensor_id = sensor_id
        self.links = links
