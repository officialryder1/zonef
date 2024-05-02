from django.shortcuts import render, redirect
from .models import Avatar, Thumbnail, Result
from .form import Create_Avatar
from PIL import Image
from io import BytesIO

# img = Image.open("main-image.png")
# img2 = Image.open('CM.png')

# img_copy = img.copy()

# area = ((img_copy.width - img2.width)//2, (img_copy.height - img2.height)//2)
# img_copy.paste(img2, area)

# img_copy.show()
# img.save('pasted_image.jpg')


def create_avatar(request): 
    if request.method == 'POST':
        form = Create_Avatar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avatar')
    else:
        form = Create_Avatar()
    return render(request, 'espees/avatar.html', {'form':form})

def image_processing(request):
    if request.POST:
        if request.method == 'POST':
            form = Create_Avatar(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                # image Processing
                img1 = Thumbnail.objects.get(id=2)
                # image = request.GET.get('avatar_img')

                img3 = img1.image

                ava = Avatar.objects.get(id=15)
                avatar = ava.image
                

                img = Image.open(img3)
                img2 = Image.open(avatar)

                img_copy = img.copy()

                area = ((img_copy.width - img2.width)//2, (img_copy.height - img2.height)//2)
                img_copy.paste(img2, area)

                buffer = BytesIO()
                
                img.save(buffer, format="JPEG")
                result = Result(image=buffer)
                print(buffer)
                
                result.save()
                
                return redirect('avatar')
        else:
            form = Create_Avatar()
        return render(request, 'espees/processing.html', {'form':form})
    else:
        return redirect("home")