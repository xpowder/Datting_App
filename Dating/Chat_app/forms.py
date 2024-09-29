from django import forms
from .models import UserProfile, Message

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'country', 'city', 'profile_picture', 'looking_for', 'bio', 'my_golden_rule', 'current_goal', 'games', 'how_he_look', 'fav_book']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'interests': forms.Textarea(attrs={'rows': 4}),
            'favorite_movies_songs': forms.Textarea(attrs={'rows': 4}),
        }


        def Age(self):
            age = self.clean_data_get('age')
            if age < 18:
                raise forms.ValidationError('You must bee at least 18 yers old')
            return age

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message_text']

        widget = {
            'message_text': forms.Textarea(attrs={'rows': 4}),
        }