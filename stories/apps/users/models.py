from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    full_name = CharField(_("Full Name"), blank=True, max_length=255)
    first_name = None
    last_name = None

    def __str__(self) -> str:
        return f'{self.full_name} <{self.email}>'

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
