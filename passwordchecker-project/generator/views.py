from django.shortcuts import render
import random 

# Create your views here.

def home(request):

	return render(request, 'generator/home.html')

def password(request):

	 characters = list('abcdefghijklmnopqrstuvwxyz')
	 thePassword=' '
	 length = int( request.GET.get('length'))

	 if request.GET.get('uppers'): 
	 	characters+=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

	 if request.GET.get('nums'): 
	 	characters+=list('0123456789')

	 if request.GET.get('specials'): 
	 	characters+=list('`~!@#$%^&*()+*')

	 for  x in range(length):
	  thePassword += random.choice(characters)

	 return render(request,'generator/password.html', {'password' : thePassword})


def about(request):
	return render(request,'generator/about.html')

#    path('',views.home , name='home'),
#    path('password/',views.password,name='password'),
#    path('about/',views.about,name='about')
# <input type="checkbox" name="uppers"> UPPERCASE
# <input type="checkbox" name="nums"> NUMBERS
# <input type="checkbox" name="specials"> SPECIAL CHARACTERS