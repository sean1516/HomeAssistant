"""
Show departure information from ctabustracker (Chicago Transit Authority).

For more details about this component, please refer to the documentation at
https://github.com/custom-components/sensor.ctabustracker/
"""
from datetime import timedelta
import logging
import requests

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

__version__ = '0.0.3'

_LOGGER = logging.getLogger(__name__)

CONF_API_KEY = 'api_key'
CONF_DEPARTURES = 'departures'
CONF_LINES = 'lines'
CONF_ROUTE = 'route'
CONF_STOP_ID = 'stop_id'

RESOURCE = "http://ctabustracker.com/bustime/api/v2/"
ENDPOINT = "getpredictions?key={}&rt={}&stpid={}&format=json"

TIME_BETWEEN_UPDATES = timedelta(seconds=60)

LINES = vol.Schema({
    vol.Required(CONF_STOP_ID): cv.string,
    vol.Required(CONF_ROUTE): cv.string,
    vol.Optional(CONF_DEPARTURES, default=1): cv.positive_int,
    vol.Optional(CONF_NAME): cv.string,
})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_LINES): vol.All(cv.ensure_list, [LINES]),
})


async def async_setup_platform(
        hass, config, async_add_entities, discovery_info=None):   # pylint: disable=W0613
    """Set up the sensor platform."""
    api_key = config[CONF_API_KEY]
    lines = config[CONF_LINES]

    dev = []
    for line in lines:
        api = CtaBusData(api_key, line)
        for departure in range(0, line['departures']):
            dev.append(CtaBusSensor(api, departure, line))
    async_add_entities(dev, True)


class CtaBusSensor(Entity):
    """Representation of a Home Assistant sensor."""

    def __init__(self, api, departure, config):
        """Initialize the sensor."""
        self.api = api
        self.departure = departure
        self.config = config
        self._state = None
        postfix = '' if departure == 0 else str(departure)
        self._name = "{} {}".format(
            self.config.get('name', 'CTA '+self.config['route']), postfix)

    def update(self):
        """Get the latest information."""
        try:
            self.api.update()
            data = self.api.data
            if data:
                self._state = data[self.departure].get('prdctdn')
            else:
                self._state = self._state
        except Exception:  # pylint: disable=W0703
            self._state = None
        _LOGGER.debug(self._state)

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Set sensor icon."""
        return 'mdi:bus-clock'


class CtaBusData:
    """Get the latest data and update the states."""

    def __init__(self, api_key, config):
        """Initialize the data object."""
        self.api_key = api_key
        self.config = config
        self.api = "{}{}".format(
            RESOURCE, ENDPOINT.format(
                self.api_key, self.config['route'], self.config['stop_id']))
        self._data = None

    @Throttle(TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data from ctabustracker."""
        try:
            self._data = requests.get(
                self.api).json().get('bustime-response', {}).get('prd', {})
            _LOGGER.debug(self._data)
        except Exception as error:  # pylint: disable=W0703
            _LOGGER.error(error)
            self._data = self._data

    @property
    def data(self):
        """Holds data."""
        return self._data
