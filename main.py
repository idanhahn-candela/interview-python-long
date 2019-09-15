import sys
import logging
import yaml

"""

- Part 1 (Pyramid):
-------------------
Useful link:
https://trypyramid.com/

required route:
localhost:{port}/api/{cID}/new_msg

localhost:{port}/api/{cID}/end_conversation

request.json


- Part 2 (OpenWeatherAPI):
--------------------------

API key:
- Your API key is cbb1caf94fd76561d77508f35efa6753
- Please, always use your API key in each API call

Endpoint:
- Please, use the endpoint api.openweathermap.org for your API calls
- Example of API call:
api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=cbb1caf94fd76561d77508f35efa6753

Useful links:
- API documentation https://openweathermap.org/api		

Store weather description


- Part 3:
---------


"""


class DatapathService:
    def __init__(self):

        self._log = logging.getLogger(__name__)

    def start(self):

        self._log.info("Start")
        """
        -----------------------
        -- LOGIC STARTS HERE --
        -----------------------
        """

if __name__ == '__main__':
    DatapathService().start()