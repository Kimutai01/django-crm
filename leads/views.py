from django.shortcuts import render,redirect
from .models import Lead, Agent
from .forms import LeadForm, LeadModalForm


# Create your views here.

def landing_page(request):
    return render(request, 'landing.html')

def lead_list(request):
    leads = Lead.objects.all()
    context={
        'leads':leads
    }
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    
    context={'lead':lead}
    
    return render(request,'leads/lead_detail.html', context)


def lead_create(request):
    form = LeadModalForm()
    
    if request.method == "POST":
        form = LeadModalForm(request.POST)
        if form.is_valid():
            form.save()
            print('The lead has been created')
            return redirect('leads')
    context={'form':form}
    return render(request,'leads/lead_create.html', context)

# def lead_create(request):
#     form = LeadModalForm()
    
#     if request.method == "POST":
#         form = LeadModalForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
            
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent,
#             )
#             print('The lead has been created')
#             return redirect('leads')
#     context={'form':form}
#     return render(request,'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModalForm(instance=lead)
    
    if request.method == 'POST':
         form = LeadModalForm(request.POST,instance=lead)
         if form.is_valid():
             form.save()
             return redirect('leads')
    context={'form':form}
    
    return render(request,'leads/lead_create.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('leads')
    context={'lead':lead}
    return render(request,'leads/lead_delete.html', context)


    