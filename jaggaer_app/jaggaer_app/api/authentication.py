from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example.models import CustomUserModel
import jwt
from datetime import datetime, timedelta


@csrf_exempt # Disables CSRF protection
def authentication_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUserModel.objects.get(username=username, password=password)
            token = generate_jwt_token(user)
            return JsonResponse({'message': 'Authentication successfully.', 'token': token})
        except CustomUserModel.DoesNotExist:
            return JsonResponse({'error': 'Invalid Details.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def generate_jwt_token(user_data):
    # Set the expiration time for the token (e.g., 1 day)
    expiration_time = datetime.utcnow() + timedelta(days=1)

    # Define the payload of the token
    payload = {
        'username': user_data.username,
        'mobile': user_data.mobile,
        'email': user_data.email,
        'organization': user_data.organization,
        'exp': expiration_time
    }

    file_path = "D:\projects\django\private.pem"

    # Load the public PEM file
    with open(file_path, 'rb') as pem_file:
        private_pem = pem_file.read()

    # Generate the JWT token using the private key
    token = jwt.encode(payload, private_pem, algorithm="RS256")

    return token