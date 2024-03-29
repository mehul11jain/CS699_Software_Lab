def indexFunc(request):
    """
    It is the main function of our project. Includes following steps:

	1)First, it authenticates user, if not valid then it is redirected to login page
	2)Takes user query to be processed.
	3)Calls Grammar-Correction Api. and fetches api-result in Json-format
	4)Uses Api result to highlight errors and make dictionary of error-data and returns to html page for rendering     

    .. note::
        | The API output is list of dictionary , where each dictionary contains error details and how to correct it.
	|        
	| Attributes of Dictionary:
	|        
	| -offset:Position of error in user input string.
        | -length:length of error(starting from offset) in user input string.
        | -message:What type of error is specified.
        | -replacement:String to replaced with, to correct error.
    

    :return: dictionary containing error-details
    :rtype: dict
    """ 
    if request.method=='GET':
        if request.user.is_authenticated:    
            return render(request,'index.html')
        else:
            return redirect("http://127.0.0.1:8000/accounts/login")
    else:
        if(request.POST.get('email') is not None and request.POST.get('pass') is not None ):
            username=request.POST.get('email')
            password=request.POST.get('pass')
            print(username)
            print(password)
            user=authenticate(username=username,password=password)
            print(user)
            if(user is not None):
                login(request, user)
                return render(request,'index.html')
            else:
                return render(request,'registration/login.html')
        else:
            query=request.POST.get('hid',None)
            query=query.capitalize()
            hquery=query
            print(hquery)
            hquery=hquery.replace('<br>',"\n")
            hquery=hquery.replace('&nbsp;','')  
            print(hquery)
            fetch = api.check(query,api_url='https://languagetool.org/api/v2/',lang='en-US')
            hcurrentText=hquery
            errorlist=[]
            message=[]
            details=[]
            errorHtml=[]
            c=0
            delta=0
            for errors in fetch['matches']:
                internalDict={}
                internalDict['offset']=errors['offset']
                internalDict['length']=errors['length']
                internalDict['text']=errors['context']['text']
                internalDict['message']=errors['message']
                internalDict['shortMessage']=errors['shortMessage']
                message.append(internalDict['shortMessage'])
                errorHtml.append(query[internalDict['offset']:internalDict['offset']+internalDict['length']])            
                details.append(internalDict['message'])
                internalDict['replacement']=[]
                limit=len(errors['replacements'])
                if limit > 7:
                    limit=7
                for i in errors['replacements'][:limit]:
                    internalDict['replacement'].append(i['value'])
                errorlist.append(internalDict)
                #print(internalDict["replacement"])
                
            for errorIndex in range(len(errorlist)):
                addFirst="<span style='background-color: rgb(255, 153, 171); padding:3px;' id='"+str(c)+"' name='replacePosition'>"
                addLast="</span>" 
                offset= errorlist[errorIndex]['offset']+delta
                length= errorlist[errorIndex]['length']
                hcurrentText=hcurrentText[:offset]+addFirst+hcurrentText[offset:offset+length]+addLast+hcurrentText[offset+length:]
                delta=delta+len(addFirst+addLast)
                c=c+1
            res=hcurrentText  
            replacements=[]
            for i in errorlist:
                replacements.append(i['replacement'])
            return render(request,'index.html',{'result':res,'sug':replacements,'details':details,'brief':message,'length':range(len(replacements)),'errorHtml':errorHtml})

