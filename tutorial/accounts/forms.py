#Suppose we want to add more option in our form like name address or email id in our "REGISTARTION FORM"


from django import forms
from django.contrib.auth.models import User
#we use User as User model if for storing data rather than using it
from django.contrib.auth.forms import UserCreationForm
#we will add more option that's why we imported it, we will inherit it properties


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label ='email do bhaia', required = True) #email field become compulsory
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )



#go ahead and save the data is commit
    def save(self, commit =True):
        user = super(RegistrationForm, self).save(commit = False)
        #commmit =False it is showing that I have not finished editing the data
        #that I want to store into the model, as first_name, last_name, email was not there so we first save that then commit
        user.first_name = self.cleaned_data['first_name']#cleaned_data ensure that data should not heart data base like someone placed a script there
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user


































