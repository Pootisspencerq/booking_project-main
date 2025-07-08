from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

#def booking_view(request):
 #   if request.method == 'POST':
  #      form = BookingForm(request.POST)
   ##        form.save()
    #        return redirect('home')
    #else:
    #     form = BookingForm()
    # return render(request, 'booking.html', {'form': form})

def resources_view(request):
    return render(request, 'resources.html')
