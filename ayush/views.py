from functools import partial
import stat
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from .serializers import Eventserializer
from .models import Eventmanage
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class home(APIView):
    def get(self,request):
        return Response({'aboutus':{'msg':'Welcome user this is ayush event manager here you can add retrieve and update your event data and you can info related about your requested event '},'aboutlinks':{'/':'main page where you can add events','/event':'to get all the events','/event/type or place (category)':'To search particular event with category or place','/updateevent':'To update event','/updateevent/event id':'search particular event id and update','deleteevent/<int:id>':'delete particular event'},'how to add event':{'eventcraete':{'name':'eventname','type':'eventtype','Place':'eventplace','date':'eventdate in format YYYY-MM-DD','time':'event time in format hour:min'}}},status=status.HTTP_200_OK)

    
    def post(self,request):
        print(request.data)
        creation=Eventserializer(data=request.data)
        if creation.is_valid():
            creation.save()
            return Response({'msg':'your event has been added!!'},status=status.HTTP_201_CREATED)
        return Response({'msg':creation.errors},status=status.HTTP_403_FORBIDDEN)
    

class Eventhandle(APIView):
    def get(self,request,category=None):
        if category is not None:
            try:
                partevent=Eventmanage.objects.filter(Q(type=category)|Q(Place=category))
                serializer=Eventserializer(partevent,many=True)
                return Response(serializer.data,status=status.HTTP_302_FOUND)
            except:
                event=Eventmanage.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check category or place carefully','select category or place from ':serializer.data},status=status.HTTP_302_FOUND)
        allevent=Eventmanage.objects.all()
        serializer=Eventserializer(allevent,many=True)
        return Response({'msg':'To search event by category enter category or place name in url!!!','data':serializer.data},status=status.HTTP_302_FOUND)
    
class Editevent(APIView):
    def get(self,request,id=None):
        if id is not None:
            try:
                editableevent=Eventmanage.objects.get(id=id)
                serializer=Eventserializer(editableevent)
                return Response({'msg':serializer.data},status=status.HTTP_202_ACCEPTED)
            except:
                event=Eventmanage.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)
        event=Eventmanage.objects.all()
        serializer=Eventserializer(event,many=True)
        return Response({'msg':'To search event by category enter category or place name in url!!!','data':serializer.data},status=status.HTTP_302_FOUND)
    
    def put(self,request,id=None):
        if id is not None:
            try:
                editableevent=Eventmanage.objects.get(id=id)
                serializer=Eventserializer(editableevent,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Event has been updated'},status=status.HTTP_202_ACCEPTED)
                return Response({'msg':serializer.errors},status=status.HTTP_403_FORBIDDEN)
            except:
                event=Eventmanage.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)

    def patch(self,request,id=None):
        if id is not None:
            try:
                editableevent=Eventmanage.objects.get(id=id)
                serializer=Eventserializer(editableevent,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Event has been updated'},status=status.HTTP_202_ACCEPTED)
                return Response({'msg':serializer.errors},status=status.HTTP_403_FORBIDDEN)
            except:
                event=Eventmanage.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)
        
class Deleteevent(APIView):
    def get(self,request,id=None):
        if id is not None:
            try:
                editableevent=Eventmanage.objects.get(id=id)
                serializer=Eventserializer(editableevent)
                return Response({'msg':serializer.data},status=status.HTTP_202_ACCEPTED)
            except:
                event=Eventmanage.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)
        event=Eventmanage.objects.all()
        serializer=Eventserializer(event,many=True)
        return Response({'msg':'To search event by category enter category or place name in url!!!','data':serializer.data},status=status.HTTP_302_FOUND)
        
    def delete(self,request,id):
        try:
            delevent=Eventmanage.objects.filter(id=id)
            delevent.delete()
            return Response({'msg':'Event deleted successfully!!!'},status=status.HTTP_302_FOUND)
        except:
            event=Eventmanage.objects.all()
            serializer=Eventserializer(event,many=True)
            return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)
        