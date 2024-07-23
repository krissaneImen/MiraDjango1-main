# views.py
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import UploadFileForm
from .models import UploadedFile


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.cleaned_data['file']
            uploaded_file = UploadedFile(name=file_obj.name, file=file_obj)
            uploaded_file.save()
            return JsonResponse(form.data)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@api_view(['GET'])
def get_file(request, file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
    except UploadedFile.DoesNotExist:
        return JsonResponse({'error': 'File not found'}, status=404)
    
    return JsonResponse({'pdfUrl': uploaded_file.file.url})



# Django View for File Download
from django.http import HttpResponse, Http404
from .models import UploadedFile

def download_file(request, file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
    except UploadedFile.DoesNotExist:
        raise Http404("File does not exist")

    response = HttpResponse(uploaded_file.file.read(), content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % uploaded_file.name
    return response

from django.core.exceptions import ObjectDoesNotExist
def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        photocopie = UploadedFile.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = photocopie.file
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % photocopie.fichier.name
    
    return response

