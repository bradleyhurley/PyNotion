import requests
import json
from string import Template
from models.user import User
from models.task import Task
from models.system import System
from models.threshold import Threshold
from models.user_preferences import UserPreferences
from models.alert_perferences import AlertPerferences
from models.base_station import BaseStation
from models.devices import Device
from models.event import Event
from models.location import Location
from models.sensor import Sensor
from models.task_data import TaskData


BASE_URL = "https://api.getnotion.com/api/"
HEADERS = {'content-type': 'application/json'}
AUTH_HEADER = '{"Authorization": "Token token=${token}"}'


class PyNotion:

    def __init__(self):
        self.r = requests
        self.auth_token = None

    def get_token(self, user_name, password):
        """
        Opens a new session
        :param user_name:
        :param password:
        :return: a user object
        """
        url = "{0}users/sign_in".format(BASE_URL)
        t = Template('{"sessions": {"email": "${email}", "password": "${password}"}}')
        data = t.substitute(email=user_name, password=password)
        results = self.r.post(url, data=data, headers=HEADERS)
        if results.status_code == 200:
            return User(**results.json()['users'])
        return results.json()

    def kill_token(self):
        """
        :return: bool to indication success or failure
        """
        url = "{0}users/sign_out".format(BASE_URL)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_my_info(self, user_id):
        """
        :return: user object
        """
        url = "{}/users/{}".format(BASE_URL, user_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return User(**results['users'])

    def delete_user(self, user_id):
        url = "{}/users/{}".format(BASE_URL, user_id)
        results = self.r.get(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_sensors(self):
        """
        :return:  list of sensors
        """
        url = "{}/sensors/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        sensors = []
        for sensor in results['sensors']:
            sensors.append(Sensor(**sensor))
        return sensors

    def get_tasks(self):
        """
        :return:  list of tasks
        """
        url = "{}/tasks/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        tasks = []
        for task in results['tasks']:
            tasks.append(Task(**task))
        return tasks

    def get_task(self, task_id):
        """
        :param task_id:
        :return: task object
        """
        url = "{}/tasks/{}/".format(BASE_URL, task_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return Task(**results['tasks'])

    def delete_task(self, task_id):
        """
        :param task_id:
        :return: Boolean
        """
        url = "{}/tasks/{}/".format(BASE_URL, task_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_task_data(self, task_id, data_before, data_after):
        # ToDo - Figure out parameters
        """
        :param: data_before 2017-01-01T12:00:00.000Z
        :param: data_after 2017-01-01T12:00:00.000Z
        :param: task_id
        :return: task data
        """
        url = "{}/tasks/{}/data/?data_before={}&data_after={}".format(BASE_URL, task_id, data_before, data_after)
        header = self._get_auth_header()
        results = self.r.get(url, headers=header)
        try:
            return TaskData(**results.json()['task'])
        except KeyError as e:
            print("Unable to retrieve task data  Date format should be '2017-01-01T12:00:00.000Z'.")

    def get_systems(self):
        """
        :return: list of systems
        """
        url = "{}/systems/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        systems = []
        for system in results['systems']:
            systems.append(System(**system))
        return systems

    def get_system(self, system_id):
        """
        :param system_id:
        :return: system details
        """
        url = "{}/systems/{}/".format(BASE_URL, system_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return System(**results['systems'])

    def delete_system(self, system_id):
        """
        :return: Boolean
        """
        url = "{}/systems/{}/".format(BASE_URL, system_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_thresholds(self):
        """
        :return: list of thresholds
        """
        # ToDo - Create/Update Threshold Class
        raise NotImplementedError
        url = "{}/thresholds/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        thresholds = []
        for threshold in results['thresholds']:
            thresholds.append(Threshold(**threshold))
        return thresholds

    def get_threshold(self, threshold_id):
        """
        :param threshold_id:
        :return: threshold details
        """
        raise NotImplementedError
        url = "{}/thresholds/{}/".format(BASE_URL, threshold_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return Threshold(**results['thresholds'])

    def delete_threshold(self, threshold_id):
        """
        :param threshold_id:
        :return: Boolean
        """
        url = "{}/thresholds/{}/".format(BASE_URL, threshold_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_user_preferences(self, user_id):
        """
        :return: user preference details
        """
        url = "{}/users/{}/user_preferences/".format(BASE_URL, user_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return UserPreferences(**results['user_preferences'])

    def get_alert_preferences(self, task_id):
        """
        :param task_id:
        :return: list of alert_preferences
        """
        url = "{}/tasks/{}/alert_preferences".format(BASE_URL, task_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        alert_preferences = []
        for alert in results['alert_preferences']:
            alert_preferences.append(AlertPerferences(**alert))
        return alert_preferences

    def get_alert_preference(self, task_id, preference_id):
        """
        :param task_id:
        :param preference_id:
        :return: alert_preference details
        """
        url = "{}/tasks/{}/alert_preferences/{}/".format(BASE_URL, task_id, preference_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return AlertPerferences(**results['alert_preferences'])

    def delete_alert_preference(self, task_id, preference_id):
        """
        :param task_id:
        :param preference_id:
        :return: Boolean
        """
        url = "{}/tasks/{}/alert_preferences/{}/".format(BASE_URL, task_id, preference_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_bridges(self):
        """
        :return: list of bridges
        """
        url = "{}/base_stations/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        base_stations = []
        for base_station in results['base_stations']:
            base_stations.append(BaseStation(**base_station))
        return base_stations

    def get_bridge(self, bridge_id):
        """
        :param bridge_id:
        :return: bridge details
        """
        if bridge_id is None:
            return "Bridge ID is a required parameter"
        url = "{}/base_stations/{}/".format(BASE_URL, bridge_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return BaseStation(**results['base_stations'])

    def delete_bridge(self, bridge_id):
        """
        :param bridge_id:
        :return: Boolean
        """
        if bridge_id is None:
            return "Bridge ID is a required parameter"
        url = "{}/base_stations/{}/".format(BASE_URL, bridge_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_devices(self):
        """
        :return: list of devices
        """
        url = "{}/devices/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        devices = []
        for device in results['devices']:
            devices.append(Device(**device))
        return devices

    def get_device(self, device_id):
        """
        :return: list of devices
        """
        if device_id is None:
            return "Device Id is a required parameter"
        url = "{}/devices/{}".format(BASE_URL, device_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return Device(**results['devices'])

    def delete_device(self, device_id):
        """
        :param device_id
        :return: Boolean
        """
        if device_id is None:
            return "Device Id is a required parameter"
        url = "{}/devices/{}".format(BASE_URL, device_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def get_events(self):
        """
        :return: list of events
        """
        # ToDo - Create Event Object
        raise NotImplementedError
        url = "{}/events/".format(BASE_URL)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        events = []
        for event in results['events']:
            events.append(Event(**event))
        return events

    def get_event(self, event_id):
        """
        :param event_id:
        :return: event details
        """
        # ToDo - Create Event Object
        raise NotImplementedError
        if event_id is None:
            return "Event ID is a required parameter"
        url = "{}/events/{}/".format(BASE_URL, event_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return Event(**results['events'])

    def get_locations(self, system_id):
        """
        :param system_id
        :return: list of locations
        """
        url = "{}/systems/{}/locations/".format(BASE_URL, system_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        locations = []
        for location in results['locations']:
            locations.append(Location(**location))
        return locations

    def get_location(self, location_id, system_id):
        """
        :param system_id
        :param location_id
        :return: location object
        """
        url = "{}/systems/{}/locations/{}/".format(BASE_URL, system_id, location_id)
        results = self.r.get(url, headers=self._get_auth_header()).json()
        return Location(**results['locations'])

    def delete_location(self, location_id, system_id):
        """
        :param system_id
        :param location_id
        :return: Boolean
        """
        url = "{}/systems/{}/locations/{}/".format(BASE_URL, system_id, location_id)
        results = self.r.delete(url, headers=self._get_auth_header())
        return results.status_code == 204

    def _get_auth_header(self):
        t = Template(AUTH_HEADER)
        if self.auth_token is None:
            print("Please set PyNotion.token\np = PyNotion()\np.token = '<<token here>>'")
            exit(1)
        return json.loads(t.substitute(token=self.auth_token))
