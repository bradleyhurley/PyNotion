class TaskData:

    def __init__(self, id=None, task_type=None, temperature=None, sensor_data=None, data=None,
                 status=None):
        self.id = id
        self.task_type = task_type
        self.temperature = temperature
        self.sensor_data = sensor_data
        self.data = data
        self.status = status
