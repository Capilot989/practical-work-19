class User:
    """
    A class representing a user with personal information.

    This class stores user data including identification, nickname,
    and personal name details. It provides methods for updating user
    information and string representations.

    Attributes:
        id: Unique identifier for the user
        nick_name: User's nickname/login name
        first_name: User's first name
        last_name: User's last name (optional)
        middle_name: User's middle name (optional)
        gender: User's gender (optional)
    """
    def __init__(
            self,
            id: int,
            nick_name: str,
            first_name: str,
            last_name: str='',
            middle_name: str='',
            gender: str=''
    ) -> None:
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(
            self,
            id=None,
            nick_name=None,
            first_name=None,
            last_name=None,
            middle_name=None,
            gender=None
    ) -> None:
        if id:
            self.id = id
        if nick_name:
            self.nick_name = nick_name
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        if gender:
            self.gender = gender

    def __str__(self):
        parts = [f"ID: {self.id}", f"LOGIN: {self.nick_name}", f"NAME: {self.first_name}"]

        if self.last_name:
            parts.append(f"LAST_NAME: {self.last_name}")
        if self.middle_name:
            parts.append(f"MIDDLE_NAME: {self.middle_name}")
        if self.gender:
            parts.append(f"GENDER: {self.gender}")

        return f"User({', '.join(parts)})"

    def __repr__(self):
        return f"{self.nick_name}"
