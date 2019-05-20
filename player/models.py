from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Invitation(models.Model):
    from_user = models.ForeignKey(User,
                                  related_name="invitations_sent",
                                  on_delete=models.CASCADE
                                  )
    to_user = models.ForeignKey(User,
                                related_name="invitations_recieved",
                                on_delete=models.CASCADE,
                                verbose_name="User to invite",
                                help_text="Select a user, you want to play with"
                                )
    message = models.CharField(max_length=300, blank=True, verbose_name="Write message",
                                help_text="Write message for the user")
    timestamp = models.DateTimeField(auto_now_add=True)

# player profile model class
class Profile(models.Model):
    #image_name = models.CharField(max_length=100, blank=True, null=True)
    image_name = models.FileField(upload_to="media/profile_image/") 
    url = models.CharField(max_length=255, blank=True, null=True)

    user = models.ForeignKey(User,
                                related_name = 'user_of_image',
                                on_delete=models.CASCADE
                                )
    created_at = models.DateTimeField('Creation time', auto_now_add=True)

    updated_at = models.DateTimeField('Update time', auto_now=True)