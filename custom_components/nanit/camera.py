from homeassistant.components.camera import Camera, CameraEntityFeature

class BabyCamera(Camera):
    def __init__(self) -> None:
        super().__init__()

    async def async_turn_on(self) -> None:
        """Turn on camera."""
        return
    
    async def async_turn_off(self) -> None:
        """Turn off camera."""
        return
