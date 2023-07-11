from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example.models import CustomUserModel, OrganizationModel

@csrf_exempt # Disables CSRF protection
def add_organization_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        organization = request.POST.get('organization')

        try:
            user = CustomUserModel.objects.get(username=username)
            user.organization = organization
            user.save()
            return JsonResponse({'message': 'Organization updated successfully.'})
        except CustomUserModel.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)