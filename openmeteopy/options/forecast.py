from openmeteopy.utils.constants import *
from openmeteopy.utils.timezones import *
from .option import Option


class ForecastOptions(Option):
    API_PATH = "https://api.open-meteo.com/v1/forecast?"
    """

    The API options accepts a WGS4 coordinate and other  weather variables .
    Time always starts at 0:00 today and contains 168 hours.

    """
    def __init__(self, latitude, longitude,current_weather = False,temperature_unit = celsius,windspeed_unit =kmh ,  precipitation_unit = mm,timeformat = iso8601, timezone = UTC, past_days = 0,forecast_days = 7,start_end = False,start_date = None,end_date = None,models = auto,cell_sellection = land):
        """
        Args:
            latitude (float): Latitude (Geographical WGS84 coordiante of the location).
            longitude (float): Longitude (Geographical WGS84 coordiante of the location).
            windspeed_unit (string, optional): Other wind speed speed units: ms, mph and kn.
            precipitation_unit (string, optional): Other precipitation amount units: inch.
            timeformat (string, optional): If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. 
                                            Please note that all time is then in UTC! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date.
            timezone (string, optional): If timezone is set, all timestamps are returned as local-time and data is returned starting at 0:00 local-time. 
                                        Any time zone name from the time zone database is available under timezones.py .
            past_days (int, optional):  If past_days is set, yesterdays or the day before yesterdays data are also returned..
        Raises:
            ValueError: Raises when latitude is not between -90 and 90 degrees.
            ValueError: Raises when longitude is not between -180 and 180 degrees.
        """
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude should be between -90 and 90 degrees.")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude should be between -180 and 180 degrees.")
        
        self.latitude = latitude
        self.longitude = longitude
        self.windspeed_unit = windspeed_unit
        self.precipitation_unit = precipitation_unit
        self.timeformat = timeformat
        self.timezone = timezone
        self.current_weather = current_weather
        self.past_days = past_days
        if start_end != False :
                    self.start_date = start_date
                    self.end_date = end_date
                    self.start_end = start_end
        self.start_end = start_end
        self.forecast_days = forecast_days
        self.cell_selection = cell_sellection
        self.temperature_unit = temperature_unit
        self.models = models

    def get_api_path(self):
          return self.API_PATH

    def get_payload(self):
        payload = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timezone": self.timezone,
            "windspeed_unit":self.windspeed_unit,
            "precipitation_unit":self.precipitation_unit,
            "timeformat":self.timeformat,
            "past_days":self.past_days
            }
        return payload