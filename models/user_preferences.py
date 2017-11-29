class UserPreferences:
    def __init__(self, user_id=None, military_time_enabled=None, celsius_enabled=None, disconnect_alerts_enabled=None):
        self.user_id = user_id
        self.military_time_enabled = military_time_enabled
        self.celsius_enabled = celsius_enabled
        self.disconnect_alerts_enabled = disconnect_alerts_enabled
