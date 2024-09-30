from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class UserProfile(models.Model):
    gender_choices = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
    ]
    
    looking_choice = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=gender_choices)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    looking_for = models.CharField(max_length=6, choices=looking_choice, blank=True)
    country = models.CharField(max_length=100, default='')
    bio = models.TextField(max_length=1500, blank=True, null=True)
    current_goal = models.CharField(max_length=250, blank=True, null=True)
    games = models.CharField(max_length=100, blank=True, null=True, default='')
    my_golden_rule = models.CharField(max_length=250, blank=True, null=True)
    how_he_look = models.CharField(max_length=100, blank=True, null=True, default='')
    fav_book = models.CharField(max_length=100, blank=True, null=True, default='')
    
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class LikeDislike(models.Model):
        user_from = models.ForeignKey(User, related_name='user_from', on_delete=models.CASCADE)
        user_to = models.ForeignKey(User, related_name='user_to', on_delete=models.CASCADE)
        is_like =  models.BooleanField(default=True)
        timestamp =  models.DateTimeField(auto_now=True)

        class Meta:
            unique_together = ('user_from', 'user_to') 

        def __str__(self):
            return f"{self.user_from} {'liked' if self.is_like else 'disliked'} {self.user_to}"
    


class Match(models.Model):
        user1 = models.ForeignKey(User, related_name='match_user1', on_delete=models.CASCADE)
        user2 = models.ForeignKey(User, related_name='match_user2', on_delete=models.CASCADE)
        matched_on = models.DateTimeField(auto_now_add=True)

        class Meta:
            unique_together = ('user1', 'user2')  

        def __str__(self):
             return f"Match: {self.user1} & {self.user2}"
        

class Message(models.Model):
            send = models.ForeignKey(User, related_name='sent_message', on_delete=models.CASCADE)
            receiver = models.ForeignKey(User, related_name='receive_message', on_delete=models.CASCADE)
            message_text = models.TextField()
            sent_at = models.DateTimeField(auto_now_add=True)
            is_read = models.BooleanField(default=False)

            def __str__(self):
                return f"Message from {self.sender} to {self.receiver}"



class Preferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_age_min = models.PositiveIntegerField()
    preferred_age_max = models.PositiveIntegerField()
    preferred_gender = models.CharField(max_length=6, choices=UserProfile.gender_choices)
    preferred_city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Preferences for {self.user}"


    