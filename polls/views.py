from django.shortcuts import render,redirect,HttpResponse
from django.http import FileResponse

from .import models
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
import io
from reportlab.lib.units import inch,mm
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
# Create your views here.
from . import forms
from django.db.models import Sum
from reportlab.platypus import Table,Paragraph,TableStyle,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

cm=2.54
# class overview(CreateView):
#     model=models.account
#     fields='__all__'
#     template_name='overview.html'
    # success_url=reverse_lazy('overview')



def overview(request):
    if request.method=="POST":
        form=forms.accountForm(request.POST)
        if form.is_valid():
            form.category = request
            form.save()
        return redirect('overview')
    else:
        form=forms.accountForm()
        income=models.account.objects.filter(category='4').aggregate(income=Sum('amount')),
        expense=models.account.objects.filter(category='3').aggregate(expense=Sum('amount')),
        total=(income[0]['income']-expense[0]['expense'])
        context={
            'form':form,
            'data':models.account.objects.all(),
            'total':total
        }
        return render(request, 'overview.html',context)
    


# class list(ListView):
#     model=models.account
#     template_name='list.html'
#     context_object_name='expense'

def generate_pdf(request):
    buf=io.BytesIO()
    #create a canvas
    c=canvas.Canvas(buf,pagesize=A4,bottomup=0)
    #create a text object
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    

    #add some lines
    accounts=models.account.objects.all()

    lines=[]
    for acc in accounts:
        lines.append(f'used_in :{acc.used_in}')
        lines.append(f'category :{acc.category.name}')
        lines.append(f'amount:{acc.amount}')
        lines.append(str(acc.date)[:10])
        lines.append("============")

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='accountstatement.pdf')




