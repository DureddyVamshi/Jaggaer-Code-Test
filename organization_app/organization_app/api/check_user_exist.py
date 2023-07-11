from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example.models import UserModel
import jwt
from datetime import datetime, timedelta

@csrf_exempt # Disables CSRF protection
def check_user_exist_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # check request header has jwt or not
        if not request.headers.get('Authorization'):
            return JsonResponse({'error': 'Authorization token is missing'}, status=401)

        try:
            # decode JWT token
            status, user_data = decode_jwt_token(request.headers.get('Authorization'))
            if not status:
                return JsonResponse({'message': 'Invalid Authorization token'})

            user = UserModel.objects.get(username=user_data['username'])
            return JsonResponse({'success': True, 'message': 'You have successfully implemented the entire flow.'})
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User Not Found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def decode_jwt_token(token):

    try:
        file_path = "D:\projects\django\public.pem"

        # Load the public PEM file
        with open(file_path, 'rb') as pem_file:
            public_pem = pem_file.read()

        # Decode the JWT token using the public key
        token = jwt.decode(token, public_pem, algorithms="RS256")
        return True, token
    except Exception as e:
        return False, str(e)