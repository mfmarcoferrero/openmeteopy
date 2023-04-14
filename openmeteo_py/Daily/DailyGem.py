from openmeteo_py.Exceptions import *

class DailyGem():

    """
    Daily Parameter functions

    Aggregations are a simple 24 hour aggregation from hourly values. 

    """

    def __init__(self) :
        self.daily_params = TypedList()

    def temperature_2m_max(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Maximum  daily air temperature at 2 meters above ground
        """
        self.daily_params.append("temperature_2m_max")
        return self
    
    def temperature_2m_min(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

         	Daily maximum in UV Index starting from 0
        """
        self.daily_params.append("temperature_2m_min")
        return self

    def apparent_temperature_max(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Maximum dailt apparent temperature
        """
        self.daily_params.append("apparent_temperature_max")
        return self

    def apparent_temperature_min(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Minimum dailt apparent temperature
        """
        self.daily_params.append("apparent_temperature_min")
        return self

    def precipitation_sum(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Sum of daily precipitation
        """
        self.daily_params.append("precipitation_sum")
        return self

    def precipitation_hours(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        The number of hours with rain
        """
        self.daily_params.append("precipitation_hours")
        return self

    def weathercode(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        The most severe weather condition on a given day
        """
        self.daily_params.append("weathercode")
        return self

    def windspeed_10m_max(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Maximum wind speed  on a day
        """
        self.daily_params.append("windspeed_10m_max")
        return self

    def windgusts_10m_max(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Maximum wind gusts on a day
        """
        self.daily_params.append("windgusts_10m_max")
        return self

    def winddirection_10m_dominant(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Dominant wind direction
        """
        self.daily_params.append("winddirection_10m_dominant")
        return self

    def shortwave_radiation_sum(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        The sum of solar radiaion on a given day in Mega Joules
        """
        self.daily_params.append("shortwave_radiation_sum")
        return self
    
    def et0_fao_evapotranspiration(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field
        """
        self.daily_params.append("et0_fao_evapotranspiration")
        return self
    
    def sunrise(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Sun rise
        """
        self.daily_params.append("sunrise")
        return self
    
    def sunset(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        sunset
        """
        self.daily_params.append("sunset")
        return self
    
    def rain_sum(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Sum of daily rain
        """
        self.daily_params.append("rain_sum")
        return self
    
    def showers_sum(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Sum of daily showers
        """
        self.daily_params.append("showers_sum")
        return self
    
    def snowfall_sum(self):
        """
        Returns the Daily configuration object 
        :returns: `Hourly()`

        Sum of daily snowfall
        """
        self.daily_params.append("snowfall_sum")
        return self