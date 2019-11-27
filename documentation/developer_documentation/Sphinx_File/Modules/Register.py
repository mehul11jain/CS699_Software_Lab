def Register(request):
    """
    Its registers new user to our website and create user-account.
    
    :return: Link for authenticated user page 
    
    """ 

    if request.method == "GET":
        return render(request,'registration/Signup.html')
    else:
        User.objects.create_user(request.POST.get('firstname')+request.POST.get('lastname'), request.POST.get('email') , request.POST.get('password'))
        username = request.POST.get('firstname')+request.POST.get('lastname')
        password = request.POST.get('password')
        print(username)
        print(password)
        user=authenticate(username=username,password=password)
        print(user)
        if(user is not None):
            login(request,user)
            return redirect("http://127.0.0.1:8000/index")
        else:
            return redirect("http://127.0.0.1:8000/index")
