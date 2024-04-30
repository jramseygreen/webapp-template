from typing import List, Optional
from flask_jwt_extended import current_user

from backend.db import db
from backend.models.setting import Setting

class __SettingsController:
    # all
    def get_settings(self) -> List[Setting]:
        # Get all settings
        settings = db.session.query(Setting).filter(Setting.is_sensitive == False).all() # only include non sensitive settings
        return settings

    # read
    def get_setting(self, name: str) -> Optional[Setting]:
        # Get a specific setting by name
        setting = db.session.query(Setting).get(name) # only include non sensitive settings

        if setting and not setting.is_sensitive:
            return setting

    # update
    def update_setting(self, name: str, value: Optional[str] = None, description: Optional[str] = None) -> Optional[Setting]:
        # Update a specific setting by name
        setting = db.session.query(Setting).get(name)
        if setting and not setting.is_sensitive:
            if value is not None:
                setting.set_value(value)
            if description is not None:
                setting.description = description
            db.session.commit()
            return setting

    def update_all_settings(self, settings: list) -> List[Setting]:
        # Update all settings
        for setting_data in settings:
            if 'name' in setting_data:
                setting = db.session.query(Setting).get(setting_data['name'])
                if setting and not setting.is_sensitive:
                    if 'value' in setting_data:
                        setting.set_value(setting_data['value'])
                    if 'description' in setting_data:
                        setting.description = setting_data['description']
        db.session.commit()
        return self.get_settings()

settings_controller = __SettingsController()
