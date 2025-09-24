from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN

PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Set up Nanit from a config entry."""
    # Can do one-time init of instance that does work of speaking to devices in
    # entry.runtime_data

    await hass.config_entries.async_forward_entry_setups(config, PLATFORMS)
    return True
    
async def async_unload_entry(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(config, PLATFORMS)