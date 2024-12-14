def handle_uploaded_file(f):  
    with open('HomeApp/static/property_images/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)