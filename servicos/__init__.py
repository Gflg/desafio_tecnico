from django.contrib.auth.models import User

if not User.objects.filter(is_superuser=True).first():
    user = User.objects.create(
        username = 'admin',
        email = 'admin@mywebsite.com',
        is_superuser = True,
    )
    user.set_password('some password')
    user.save()