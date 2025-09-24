from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from .const import DOMAIN

import voluptuous as vol

DATA_SCHEMA_USER = vol.Schema(
    {
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
    },
)

DATA_SCHEMA_OTP = vol.Schema(
    {
        vol.Required("otp"): str,
    },
)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Nanit."""
    VERSION = 1
    user_info_ = None

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Attempt to log in and get OTP
            # If log in failure, raise error
            # else show form to user
            self.user_info_ = user_input
            return await self.async_step_otp()
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA_USER, errors=errors)
    
    async def async_step_otp(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Validate OTP allows connection and obtain baby device ID(s)
            return self.async_create_entry(
                title="Nanit",
                data={
                    "username": self.user_info_[CONF_USERNAME],
                    "password": self.user_info_[CONF_PASSWORD],
                    "otp": user_input["otp"]
                },
            )
        return self.async_show_form(
            step_id="otp", data_schema=DATA_SCHEMA_OTP, errors=errors)