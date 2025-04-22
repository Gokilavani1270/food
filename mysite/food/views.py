from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def index(request):
    return HttpResponse('Hellowwww ! this is Foooood Page !!!')

def item(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

class ItemClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'

def detail(request,Item_id):
    item=Item.objects.get(pk=Item_id)
    context={
        'item':item,
    }
    return render(request,'food/details.html',context)

class FoodDetail(DetailView):
    model=Item
    template_name='food/details.html'



def create_item(request):
    form=ItemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('food:item')
    return render(request,'food/item_form.html',{'form':form})

class CreateItem(CreateView):
    model=Item
    fields=['Item_name','Item_desc','Item_price','Item_image']
    template_name='food/item_form.html'
    
    def form_valid(self,form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:item')
    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('food:item')
    return render(request,'food/item_delete.html',{'item':item})

