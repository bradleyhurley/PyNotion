from PyNotion import PyNotion


def main():
    p = PyNotion()
    # First Run - Get a valid token
    user = p.get_token("notion email", "password")
    print(user.auth_token)

    # After Valid Token:
    p = PyNotion()
    p.auth_token = 'auth token'

    # Get List Of Sensors
    sensors = p.get_sensors()
    for sensor in sensors:
        print(sensor.signal_strength)
        print(sensor.created_at)
        print(sensor.rssi)
        print(sensor.hardware_revision)
        print(sensor.name)

    # Get List Of Locations
    locations = p.get_locations(system_id=9999)
    for location in locations:
        print(location.display_name)
        print(print(location.id))

    # Get List Of Bridges
    base_stations = p.get_bridges()
    for base_station in base_stations:
        print(base_station.name)

    # p.kill_token()
if __name__ == "__main__":
    main()
