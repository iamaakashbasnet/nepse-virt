from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt import authentication

from v1.data.fetcher.live_data import get_live_market
from v1.data.models import Security, SecurityData
from v1.data.serializers import livedata
from nepse import Nepse


nepse = Nepse()
nepse.setTLSVerification(False)


class FetchLiveData(APIView):
    def get(self, request):
        get_live_market()

        return Response({'result': 'fetched'})


class IsMarketOpen(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(nepse.isNepseOpen())


class LiveDataStockNameListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    queryset = Security.objects.all()
    serializer_class = livedata.LiveDataStockNameSerializer


class LiveDataListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    queryset = SecurityData.objects.all()
    serializer_class = livedata.LiveDataSerializer


class StockDetailView(RetrieveAPIView):
    serializer_class = livedata.LiveDataSerializer
    queryset = SecurityData.objects.all()

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(), id=self.kwargs.get('id'))
