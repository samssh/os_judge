from django.contrib.auth.models import User

user = User()
user.username = 'sam'
user.set_password('pass')
user.is_superuser = True
user.is_staff = True
user.save()
