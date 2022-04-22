import jwt

encodeToken = jwt.encode({"Name": "Shivansh"}, "Privacy and security project", algorithm="HS256")
print(encodeToken)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoiU2hpdmFuc2gifQ.R4y7f6fX1j8iaXAJw7C8rHgIyqpL_xVVaLpvJhnsxeA
res = jwt.decode(encodeToken, "Privacy and security project", algorithm="HS256")
print(res)