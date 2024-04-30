from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from backend.db import db

class Setting(db.Model):
    serialize_rules = ('-type', '-is_sensitive')

    name: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String, nullable=True)
    type: Mapped[str] = mapped_column(String)
    is_sensitive: Mapped[bool] = mapped_column(Boolean, default=False)

    # Convert the string value back to the intended type
    def get_value(self):
            if self.type == 'int':
                return int(self.value)
            elif self.type == 'bool':
                return self.value.lower() in ['true', '1', 't']
            elif self.type == 'str':
                return self.value
            else:
                raise ValueError(f"Unsupported type {self.type}")

    # Convert the value to string and set the type appropriately
    def set_value(self, value):
        if isinstance(value, bool):
            self.type = 'bool'
            self.value = 'true' if value else 'false'
        elif isinstance(value, int):
            self.type = 'int'
            self.value = str(value)
        elif isinstance(value, str):
            self.type = 'str'
            self.value = value
        else:
            raise ValueError("Unsupported type")

    # Override to_dict to convert types appropriately
    def to_dict(self):
        serialized = super().to_dict()
        serialized['value'] = self.get_value()  # Convert value to its original type
        return serialized
