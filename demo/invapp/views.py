from django.shortcuts import render, HttpResponse
from .models import Varastot, Tuote
from django.contrib.auth.models import User
from .serializers import VarastotSerializer, TuoteSerializer, UserSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    return render(request, "home.html")

def varasto(request):
    omatvarastot = Varastot.objects.all()
    tuotteet = Tuote.objects.select_related("ean_koodi").all()

        
    return render(request, "varasto.html", {"varastot": omatvarastot, "tuotteet": tuotteet})


class TuoteViewSet(viewsets.ModelViewSet):
    queryset = Tuote.objects.all()
    serializer_class = TuoteSerializer
    lookup_field = 'ean_koodi'

    @action(detail=True, methods=['get'])
    def skannaa(self, request, ean_koodi=None):
        tuote = Tuote.objects.get(ean_koodi=ean_koodi)
        if not tuote:
            return Response({"error": "Tuotetta ei löydy"}, status=404)
        else:
            serializer = self.get_serializer(tuote)

            return Response(serializer.data)
        

class VarastotViewSet(viewsets.ModelViewSet):
    serializer_class = VarastotSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Varastot.objects.filter(kayttaja=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(kayttaja=self.request.user)

    @action(detail=False, methods=['get'])
    def vanhentuvat(self, request):
        
        tanaan = datetime.now().date()
        alle_3_pv = tanaan + timedelta(days=3)

        queryset = Varastot.objects.filter(kayttaja=request.user, viimeinen_käyttöpäivä__range=[tanaan, alle_3_pv]).order_by('viimeinen_käyttöpäivä')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]