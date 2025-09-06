from .base import MFPBase


class Friend(MFPBase):
    """Represents a friend in MyFitnessPal."""

    def __init__(
        self,
        username: str,
        last_login: str,
        hidden: bool,
        position: int,
        main_image_thumb_path: str,
    ):
        self._username = username
        self._last_login = last_login
        self._hidden = hidden
        self._position = position
        self._main_image_thumb_path = main_image_thumb_path

    @property
    def hidden(self) -> bool:
        """Returns whether the friend is hidden."""
        return self._hidden

    @property
    def username(self) -> str:
        """Returns the username of the friend."""
        return self._username

    @property
    def last_login(self) -> str:
        """Returns the last login date of the friend."""
        return self._last_login

    @property
    def position(self) -> int:
        """Returns the position of the friend in the friend list."""
        return self._position

    @property
    def main_image_thumb_path(self) -> str:
        """Returns the thumbnail path of the friend's main image."""
        return self._main_image_thumb_path

    def __str__(self) -> str:
        return f"Friend(username={self.username}, last_login={self.last_login}, hidden={self.hidden}, position={self.position}, main_image_thumb_path={self.main_image_thumb_path})"
