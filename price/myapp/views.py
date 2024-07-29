# myapp/views.py
from rest_framework.decorators import api_view, permission_classes
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings
from .models import Alert
from .serializers import AlertSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User

# View to create an alert
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_alert(request):
    user = request.user
    target_price = request.data.get('target_price')
    email = request.data.get('email')

    alert = Alert(user=user, target_price=target_price, statement='non-triggered', email=email)
    alert.save()

    return Response({'message': 'Alert created successfully'}, status=status.HTTP_201_CREATED)

# View to delete an alert
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_alert(request, pk):
    alert = get_object_or_404(Alert, pk=pk)
    if request.user != alert.user:
        return Response({'error': 'You are not authorized to delete this alert'}, status=status.HTTP_403_FORBIDDEN)
    
    alert.delete()
    return Response({'message': 'Alert deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# View to fetch alerts
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_alerts(request):
    statement = request.query_params.get('statement')
    cache_key = f"alerts_{request.user.id}_{statement}" if statement else f"alerts_{request.user.id}"

    cached_alerts = cache.get(cache_key)
    if cached_alerts:
        return Response(cached_alerts)

    if statement:
        alerts = Alert.objects.filter(user=request.user, statement=statement)
    else:
        alerts = Alert.objects.filter(user=request.user)
    
    paginator = PageNumberPagination()
    paginated_alerts = paginator.paginate_queryset(alerts, request)
    serializer = AlertSerializer(paginated_alerts, many=True)
    
    response_data = paginator.get_paginated_response(serializer.data).data

    # Cache the response data
    cache.set(cache_key, response_data, timeout=300)  # Cache for 5 minutes

    return Response(response_data)
  

# View to process alerts (to be called by the WebSocket script)
@api_view(['POST'])
def process_alerts(request):
    current_price = request.data.get('current_price')
    if current_price is None:
        return Response({'error': 'Current price not provided'}, status=status.HTTP_400_BAD_REQUEST)

    alerts = Alert.objects.filter(statement='non-triggered')
    for alert in alerts:
        if float(current_price) >= alert.target_price:
            send_mail(
                'Bitcoin Price Alert',
                f'The Bitcoin price has reached your target of {alert.target_price}.',
                settings.DEFAULT_FROM_EMAIL,
                [alert.email],
            )
            alert.statement = 'triggered'
            alert.save()

    return Response({'message': 'Alerts processed successfully'})

