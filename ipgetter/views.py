import requests
from django.http import JsonResponse
from .models import User

def get_ip(request):
    """Retrieve user IP and fetch geolocation details."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    # Fetch details using an external API
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,city,isp,query")
    data = response.json()

    if data["status"] == "fail":
        return JsonResponse({"error": "Failed to retrieve IP details"})

    # Save user IP and details in the database
    user, _ = User.objects.get_or_create(ip_address=ip)
    user.country = data.get("country", "Unknown")
    user.city = data.get("city", "Unknown")
    user.isp = data.get("isp", "Unknown")
    user.save()

    return JsonResponse({
        "ip": ip,
        "country": data.get("country", "Unknown"),
        "city": data.get("city", "Unknown"),
        "isp": data.get("isp", "Unknown"),
    })

