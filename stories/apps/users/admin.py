from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _
from image_cropping import ImageCroppingMixin

from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm
from .models import User


admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)


@admin.register(User)
class UserAdmin(ImageCroppingMixin, auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("full_name", "email")}),
        (_("Profile picture"), {"fields": ("image", "cropping")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "full_name", "email", "is_superuser"]
    search_fields = ["username", "full_name", "email"]
