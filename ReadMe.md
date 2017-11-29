## PyNotion

PyNotion is designed to be a simple to use Python wrapper around the Notion API.


- ##### Learn More About Notion Sensors:
    - [Notion](http://getnotion.com/)

- ##### Read The Notion API Docs
    - [Notion API Documentation](https://docs.getnotion.com/)
    

### Setup:
Create a Python 3 Virtual Environment
- [Virtual Environment Reference](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```bash
pip install -r requirements.txt
```

### Sample Usage:
```python
from PyNotion import PyNotion

p = PyNotion()
# First Run - Get a valid token
user = p.get_token("notion email", "password")
print(user.auth_token)
p.auth_token = user.auth_token

sensors = p.get_sensors()
for sensor in sensors:
    print(sensor.name)
```

```python
from PyNotion import PyNotion

p = PyNotion()
p.auth_token = 'notion auth token'
```

```python
# When Finished:
p.kill_token()
```

### Known Issues / Limitations:
- Python 3 Only (I have no plans on supporting Python 2)
- The following methods have not been implemented:
    - get_thresholds
    - get_threshold
    - get_events
    - get_event
- The wrapper currently does not support update operations.

##### I am in no way affiliated with Notion, nor is this an officially supported product.