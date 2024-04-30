from typing import List, Optional
from backend.composables.response import response
from backend.controllers.settings_controller import settings_controller
from backend.server import server

class __SettingsService:
    # all
    def get_settings(self):
        settings = settings_controller.get_settings()
        return response.ok('Retrieved all settings successfully', [setting.to_dict() for setting in settings])

    # read
    def get_setting(self, name: str):
        # Get a specific setting by name
        setting = settings_controller.get_setting(name)
        if setting:
            return response.ok('Retrieved setting successfully', setting.to_dict())
        return response.not_found('Setting not found')

    # update
    def update_setting(self, name: str, value: Optional[str] = None, description: Optional[str] = None):
        # Update a specific setting by name
        setting = settings_controller.update_setting(name, value, description)
        if setting:
            return response.ok("Setting updated successfully", setting.to_dict())
        return response.not_found("Setting not found")

    def update_all_settings(self, settings: list):
        # Update all settings
        settings = settings_controller.update_all_settings(settings)
        return response.ok("Settings updated successfully", [setting.to_dict() for setting in settings])

settings_service = __SettingsService()
