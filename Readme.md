# Add organization
```
curl --location 'http://127.0.0.1:8000/api/add_organization/' \
--form 'username="Tony"' \
--form 'organization="Google"'
```

# Authentication
```
curl --location 'http://127.0.0.1:8000/api/authentication/' \
--form 'username="john"' \
--form 'password="john123"'
```

# Validate User
```
curl --location --request POST 'http://127.0.0.1:8000/api/check_user_exist/' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvaG4iLCJtb2JpbGUiOiIxMTExMTExMTExIiwiZW1haWwiOiJqb2huQGdtYWlsLmNvbSIsIm9yZ2FuaXphdGlvbiI6bnVsbCwiZXhwIjoxNjg5MTk3MDUzfQ.LYzTUwyDZhv4l47LD5T-ynlwnPFmM-_mT8ytCzCljtyA9FPelFOkqwmW8VShLofwiHpU78j_NWiZCr-moDs2-30tkmz9i8bdrX1_Q0BxYRuWtx1TyUtbONL2PkkN9vAWzjFXhTqqn_g7vrJp2IqCtSj1O0eVwixjDojGpuGBdgE'
```

Also provided the mysql database schema files along with project code.