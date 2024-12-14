from django import forms 
from .models import AgentsInfo, property,Enquiry,Agents,Contact_User


class RegisterForm(forms.Form):
    email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control mx-2','name':'email','placeholder':'email'}))
    password=forms.CharField(max_length=128,label="password",widget=forms.PasswordInput(attrs={'class':'form-control mx-2','name':'password','placeholder':'password'}))
    username=forms.CharField(max_length=30,label="username",widget=forms.TextInput(attrs={'class':'form-control mx-2','name':'username','placeholder':'username'}))

class LoginForm(forms.Form):
    password=forms.CharField(max_length=128,label="password",widget=forms.PasswordInput(attrs={'class':'form-control mx-2','name':'password','placeholder':'password'}))
    username=forms.CharField(max_length=30,label="username",widget=forms.TextInput(attrs={'class':'form-control mx-2','name':'username','placeholder':'username'}))

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder': ''})

PROPERTY_TYPE_CHOICES = [
    ('Commercial Space', 'Commercial Space'),
    ('Flat/Apartment/House', 'Flat/Apartment/House'),
    ('Plot/Land', 'Plot/Land'),
    ('Agricultural Land', 'Agricultural Land'),
    ('PG/Co-Living', 'PG/Co-Living'),
    ('Industrial Land', 'Industrial Land'),
    ('Farmland', 'Farmland'),
]
Property_action=[
    ('rent','rent'),
    ('sell','sell'),
]

class PostPropertyForm(BootstrapModelForm):
    class Meta:
        model = property
        fields='__all__'
        exclude=["owner_id","property_id","updated","created","owner_email"]
        bedrooms=forms.IntegerField(required=False)
        bathrooms=forms.IntegerField(required=False)
        widgets = {
            'type': forms.Select(choices=PROPERTY_TYPE_CHOICES,attrs={'class': 'form-select'}),
            'action': forms.Select(choices=Property_action,attrs={'class': 'form-select'}),
            'furnished': forms.Select(attrs={'class': 'form-select'}),
            'description':forms.Textarea(attrs={'rows':'2','cols':'2'})
        }
        
class EnquiryForm(BootstrapModelForm):
    class Meta:
        model = Enquiry
        fields='__all__'
        exclude=["sender_id","reciever_id","property","posted_on"]
        
class UpdateForm(BootstrapModelForm):
    
    class Meta:
        model = property
        fields=('image',)
        
        
class AgentRegisterForm(BootstrapModelForm):
    class Meta:
        model = Agents
        fields='__all__'
        exclude=["agent_id"]
        widgets = {
            'password': forms.PasswordInput()   
        }
        
class AgentLoginForm(forms.Form):
    password=forms.CharField(max_length=128,label="password",widget=forms.PasswordInput(attrs={'class':'form-control mx-2','name':'password','placeholder':'password'}))
    username=forms.CharField(max_length=30,label="username",widget=forms.TextInput(attrs={'class':'form-control mx-2','name':'username','placeholder':'username'}))

class AgentProfileForm(BootstrapModelForm):
    class Meta:
        model = AgentsInfo
        fields='__all__'
        exclude=["agent_id","joined_on"]
        widgets = {
          "agent_email":forms.EmailInput(),
          "image":forms.FileInput()
        }

class AgentImageUpload(BootstrapModelForm):
     class Meta:
        model = AgentsInfo
        fields=('image',)
      
class UserContactForm(BootstrapModelForm):
    class Meta:
        model=Contact_User
        fields='__all__'
        exclude=["member_id",'date']
        widgets = {
            'message':forms.Textarea(attrs={'rows':'2','cols':'2'})
        }