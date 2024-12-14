from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from .models import Agents, members,property,Enquiry,AgentsInfo
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from .forms import AgentLoginForm, AgentRegisterForm, RegisterForm,LoginForm,PostPropertyForm,UserContactForm,EnquiryForm, UpdateForm,AgentProfileForm,AgentImageUpload

# Create your views here

def index(request):
    user_obj=None
    propertys=property.objects.all()[:4]
    agents=AgentsInfo.objects.all()[:4]
    
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request, 'index.html', {'user':user_obj,'propertys':propertys,'agents':agents})
    except:
        return render(request,'index.html',{'propertys':propertys,'agents':agents})

def aboutus(request):
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'aboutus.html',{'user':user_obj})
    except:
        return render(request,'aboutus.html')

def contact_us(request):
    
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            form=UserContactForm(request.POST, request.FILES)
            if request.method=='POST':
                if form.is_valid():
                    form.instance.member_id=user_obj
                    form.save()
                    messages.success(request,"Thankyou for contacting us. We will get back to you soon...")
                    return redirect('index')                  
                else:
                    messages.error(request,"Form is invalid")
            return render(request,'contactform.html',{'user':user_obj,'form':form})
    except:
        return redirect('login')

def properties(request):
    propertys=property.objects.all()
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})    

def plots(request):
    propertys=property.objects.filter(type__contains="Land")
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def flats(request):
    propertys=property.objects.filter(type="Flat/Apartment/House")
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def rent(request):
    propertys=property.objects.filter(action="rent")
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def buy(request):
    propertys=property.objects.filter(action='sell')
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def pg_coliving(request):
    propertys=property.objects.filter(type="PG/Co-Living")
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def AgriculturalLand(request):
    propertys=property.objects.filter(type="Agricultural Land")
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def CommercialSpace(request):
    propertys=property.objects.filter(type="Commercial Space")
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            return render(request,'property.html',{'propertys':propertys,'user':user_obj})    
    except:
        return render(request,'property.html',{'propertys':propertys})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        mem=members(email=email,password=password,username=username)
        mem.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})
  
def login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        next=request.POST['next']
        user = members.objects.filter(username=username, password=password).exists()
        if user:
            request.session["session_key"] = username
            if next!="":
                return redirect(next)
            else:
                return redirect('index')
        else:
            messages.error(request, 'Wrong Credentials')
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})


def postproperty(request):
    key = request.session.get("session_key")
    if key:
        owner = members.objects.get(username=key)
        if request.method == 'POST':
            form = PostPropertyForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.owner_id = owner 
                form.instance.owner_email=owner.email
                form.save()
                
                messages.success(request, "Property uploaded successfully")
                return redirect('index')
            else:
                messages.error(request, "Form is invalid")
        else:
            form = PostPropertyForm()
    else:
        messages.error(request, "User session not found")
        return redirect('login')
    
    return render(request, 'postproperty.html', {'form': form, 'user':owner})

def view_details(request,property_id):
    details=property.objects.get(property_id=property_id)
    agents=AgentsInfo.objects.filter(operating_city__contains=details.city)
    form=EnquiryForm()
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            context = {'details': details,'form':form,'agents':agents,'user':user_obj}
            return render(request,'property_details.html',context)
    except:
        context = {'details': details,'form':form,'agents':agents}
        return render(request,'property_details.html',context)

def view_posted_property(request):
    key = request.session.get("session_key")
    if key:
        return redirect('view')
    else:
        messages.error(request,"You need to login")
        return redirect('login')
    
def view(request):
    key = request.session.get("session_key")
    user = members.objects.get(username=key)
    member_id=user.member_id
    details=property.objects.filter(owner_id=member_id)
    context = {'details': details,'user':user}
    return render(request,'posted_property_view.html',context)

def enquiry(request,property_id):
    if request.method == 'POST':
        key = request.session.get("session_key")
        next=request.POST['next']
        if key:
            user_obj = members.objects.get(username=key)
            prp=property.objects.get(property_id=property_id)
            form = EnquiryForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.sender_id = user_obj
                form.instance.property=prp
                form.instance.reciever_id=prp.owner_id
                form.save()
                messages.success(request, "Enquiry posted!")
                return redirect('view_details',property_id=property_id)
            else:
                messages.error(request, "Form is invalid")
    
        else:
            messages.error(request, "User session not found")
            form=LoginForm()
            #return redirect(reverse('login',{'next_url':next_url}))
            return render(request,'login.html',{'form':form,'next':next})
    else:
        form = EnquiryForm()
        return redirect('view_details',property_id=property_id)
    return redirect('view_details',property_id=property_id)


def enquired_property(request):
    key = request.session.get("session_key")
    if key:
        id=members.objects.get(username=key)
        records=Enquiry.objects.filter(reciever_id=id)
        context={'records':records,'user':id}
        return render(request,'enquired_property.html',context)
        
    return redirect('login')

def update_property(request,property_id):

    details = get_object_or_404(property, property_id=property_id)
    if request.method=='POST':
        form=UpdateForm(request.POST,request.FILES,instance=details)
        if form.is_valid():
            type=request.POST['type']
            price=request.POST['price']
            location=request.POST['location']
            area=request.POST['area']
            description=request.POST['description']
            action=request.POST['action']
            details.updated=date.today()
            name=request.POST['name']
            contact=request.POST['contact']
            title=request.POST['title']
            owner_email=request.POST['owner_email']
            furnished=request.POST['furnished']
            bedrooms=request.POST['bedrooms']
            bathrooms=request.POST['bathrooms']
            city=request.POST['city']
            state=request.POST['state']
            
            details.title=title
            details.type=type
            details.price=price
            details.location=location
            details.area=area
            details.description=description
            details.city=city
            details.state=state
            details.action=action
            details.name=name
            details.contact=contact
            details.owner_email=owner_email
            details.furnished=furnished
            details.bedrooms=bedrooms
            details.bathrooms=bathrooms
            details.save()
            form.save()
            messages.success(request,'Property Details updated!!!')
            return redirect('view_details',details.property_id)
    else:
        price=details.price
        form=UpdateForm(request.POST,request.FILES,instance=details)
           
        try:
            if request.session["session_key"]!=None:
                user_details = request.session.get("session_key")
                user_obj = members.objects.get(username=user_details)
                context = {'details': details,'form':form,'user':user_obj}
                return render(request,'update_property.html',context)
        except:    
            context = {'details': details,'form':form} 
            return render(request,'update_property.html',context)
  
def delete_property(request,property_id):
    prp=property.objects.get(property_id=property_id)
    prp.delete()
    return redirect('view_posted_property')

  
def search(request):
    if request.method=='POST':
        type=request.POST['type']
        location=request.POST['location']
        min=request.POST['min']
        max=request.POST['max']
        area=request.POST['area']
        
        properties=property.objects.filter(type=type,city=location,price__gte=min,price__lte=max,area__gte=area)
        return render(request,'searchproperty.html',{'properties':properties})
    
def logout(request):
    django_logout(request)
    return redirect('index')


def agent_register(request):
    form = AgentRegisterForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Agent Registration Successful!!!")
        else:
            messages.error(request, "Form is invalid")
        return redirect('agent_login')
    return render(request, 'agents/agentregister.html', {'form': form})

def agent_login(request):
    form = AgentLoginForm(request.POST,request.FILES)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = Agents.objects.filter(username=username, password=password).exists()
        if user:
            request.session["session_key"] = username
            return redirect('agentdashboard')
        else:
            messages.error(request, 'Wrong Credentials')
            return render(request, 'agentlogin.html', {'form': form})

    return render(request, 'agents/agentlogin.html', {'form': form})


def agentdashboard(request):
    try: 
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user = Agents.objects.get(username=user_details)
            propertys=property.objects.all()[:4]
            return render(request,'agents/agentdashboard.html',{'user':user,'propertys':propertys})
    except:
        return redirect('agent_login')
   
def fill_profile(request):
    user = Agents.objects.get(username=request.session.get("session_key"))

    form=AgentProfileForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.instance.agent_id = user
            form.save()
            messages.success(request,'Agent Info Posted!')
            return redirect('agentdashboard')

        else:
            messages.error(request,'form is not valid!')
    else:
        return render(request,'agents/fillprofile.html',{'form':form,'user':user})

def viewprofile(request):
    user = Agents.objects.get(username=request.session.get("session_key"))
    try:
        info=AgentsInfo.objects.get(agent_id=user.agent_id)
        return render(request,'agents/viewprofile.html',{'user':user,'info':info})
    except AgentsInfo.DoesNotExist:
        messages.error(request,'Your profile is not complete , you must complete your profile first.')
        return redirect('fill_profile')
            

def view_all_property(request):
    user = Agents.objects.get(username=request.session.get("session_key"))
    propertys=property.objects.all()
    
    return render(request,'agents/view_all_property.html',{'user':user,'propertys':propertys})

def editProfile(request):
    user = Agents.objects.get(username=request.session.get("session_key"))
    try:
        info=AgentsInfo.objects.get(agent_id=user.agent_id)
        form=AgentImageUpload(request.POST,request.FILES,instance=info)
        if request.method=='POST':
            if form.is_valid():
                name=request.POST['name']
                contact=request.POST['contact']
                email=request.POST['email']
                city=request.POST['city']
                address=request.POST['address']
                Operating_cities=request.POST['Operating_cities']
                Operating_Location=request.POST['Operating_Location']
                dealing_areas=request.POST['dealing_areas']
                operating_since=request.POSt['operating_since']
                
                info.agent_email=email
                info.agent_contact=contact
                info.agent_name=name
                info.address=address
                info.operating_city=Operating_cities
                info.operating_locations=Operating_Location
                info.city=city
                info.deals_in=dealing_areas
                info.operating_since=operating_since
                info.save()
                form.save()
                user.email=email
                user.save()
                messages.success(request,'Agent Info Updated!')
                return redirect('agentdashboard')
            
        else:
            return render(request,'agents/editprofile.html',{'user':user,'info':info,'form':form})
    except AgentsInfo.DoesNotExist:
        messages.error(request,'Your profile is not complete , you must complete your profile first.')
        return redirect('fill_profile')

def details(request,property_id):
    user = Agents.objects.get(username=request.session.get("session_key"))
    details=property.objects.get(property_id=property_id)
    form=EnquiryForm()
    context = {'details': details,'form':form,'user':user}
    return render(request,'agents/details.html',context)

def beginner_guide(request):
    user = Agents.objects.get(username=request.session.get("session_key"))
    return render(request,'agents/guide.html',{'user':user})

def view_agent_details(request,agent_id):
    details=AgentsInfo.objects.get(agent_id=agent_id)    
    context = {'details': details}
    return render(request,'agent_details.html',context)

def view_agents(request):
    agents=AgentsInfo.objects.all()
    try:
        if request.session["session_key"]!=None:
            user_details = request.session.get("session_key")
            user_obj = members.objects.get(username=user_details)
            context={'agents':agents,'user':user_obj}
            return render(request,'viewagents.html',context)
    except:
        context={'agents':agents}
        return render(request,'viewagents.html',context)