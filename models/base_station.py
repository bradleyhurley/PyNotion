class BaseStation:

    def __init__(self, id=None, name=None, mode=None, hardware_id=None, firmware_version=None, hardware_revision=None,
                 missing_at=None, created_at=None, updated_at=None, system_id=None,
                 organization=None, system=None, firmware=None, links=None):
        self.id = id
        self.name = name
        self.mode = mode
        self.hardware_id = hardware_id
        self.firmware_version = firmware_version
        self.hardware_revision = hardware_revision
        self.missing_at = missing_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.system_id = system_id
        self.organization = organization
        self.system = system
        self.firmware = firmware
        self.links = links
