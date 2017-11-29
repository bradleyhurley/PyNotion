class Sensor:
    def __init__(self, id=None, uuid=None, user=None, bridge=None, last_bridge_hardware_id=None, name=None,
                 location_id=None, system_id=None, hardware_id=None, firmware_version=None, hardware_revision=None,
                 device_key=None, installed_at=None, calibrated_at=None, last_reported_at=None, missing_at=None,
                 updated_at=None, created_at=None, signal_strength=None, links=None, encryption_key=None, lqi=None, rssi=None):
        self.id = id
        self.uuid = uuid
        self.user = user
        self.bridge = bridge
        self.last_bridge_hardware_id = last_bridge_hardware_id
        self.name = name
        self.location_id = location_id
        self.system_id = system_id
        self.hardware_ud = hardware_id
        self.firmware_verison = firmware_version
        self.hardware_revision = hardware_revision
        self.device_key = device_key
        self.installed_at = installed_at
        self.calibrated_at = calibrated_at
        self.last_reported_at = last_reported_at
        self.missing_at = missing_at
        self.updated_at = updated_at
        self.created_at = created_at
        self.signal_strength = signal_strength
        self.links = links
        self.encryption_key = encryption_key
        self.lqi = lqi
        self.rssi = rssi
