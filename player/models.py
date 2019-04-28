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
