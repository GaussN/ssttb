from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from education.models import Test


@login_required
@user_passes_test(lambda user: user.is_superuser)
def test_view(request: HttpRequest, id):
    return render(request, 'admin_panel/test.html', {'test': Test.objects.get(pk=id)})
