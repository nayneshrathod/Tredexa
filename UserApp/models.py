from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    password = models.CharField(max_length=120, null=True, blank=True)
    username = models.CharField(max_length=120, null=True, blank=True)

    #
    # class Meta:
    #     app_label = 'default'

    class Meta:
        app_label = 'UserApp'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    #
    class Meta:
        app_label = 'UserApp'


'''

class UserRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'User_Database':
            return 'User_db'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'User_Database':
            return 'User_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'User_Database' and obj2._meta.app_label == 'User_Database':
            return True
        # Allow if neither is chinook app
        elif 'User_Database' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'User_db' or model._meta.app_label == "User_Database":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True
            
'''
