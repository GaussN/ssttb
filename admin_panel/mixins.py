from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class SuperuserTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('/login/?next=/admin/')
