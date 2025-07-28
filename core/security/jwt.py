#
# Author: Rohtash Lakra
#
# Reference: https://pyjwt.readthedocs.io/en/stable/usage.html

import base64
import hashlib
import hmac
import json
from datetime import datetime, timezone, timedelta
import jwt

UTF_8 = "utf-8"

# “exp” (Expiration Time) Claim
EXPIRATION_TIME = "exp"
# “nbf” (Not Before Time) Claim
NOT_BEFORE_TIME = "nbf"
# “iss” (Issuer) Claim
ISSUER = "iss"
# “aud” (Audience) Claim
AUDIENCE = "aud"
# “iat” (Issued At) Claim
ISSUED_AT = "iat"

class JwtUtils:
    pass

# secret = "<API_KEY_SHARED_SECRET>".encode(encoding)
# secret = "2C16E184-70E5-4475-842D-64252329C7DE".encode(UTF_8)
# Api-Key: 7013b86ad3d44a08b9c21c5325223504
secret = "da205fe5ed8ae3abee3bb317d05d9784ee44f0989c92da2fd0fe507c0c159b6846822506ecdfef77ccc01afab3aaf8e8d4cac26582bfa1c7b8d1c5f1b099340e".encode(UTF_8)
# epoch_time
iat = datetime.now(tz=timezone.utc)
# print(f"iat={iat}, {int(iat.timestamp())}")
# expiry in next 15 mins
# exp = iat + timedelta(seconds=(60 * 15))
exp = iat + timedelta(minutes=15)
# print(f"exp={exp}, {int(exp.timestamp())}")

JWT_HEADER = json.dumps(
    {
        "alg": "HS256",
        "typ": "JWT"
    }, separators=(",", ":")
).encode(UTF_8)

jwt_payload = json.dumps(
    {
        "aud": "b2d0189f3a4442709472e7e313499286",
        "iss": "Lakra",
        "iat": int(iat.timestamp()),
        "exp": int(exp.timestamp()),
        "sub": "b2d0189f3a4442709472e7e313499286",
        "email": "rslakra@gmail.com",
        "type": "access_token"
    }, separators=(",", ":")
).encode(UTF_8)

encoded_header_bytes = base64.urlsafe_b64encode(JWT_HEADER).replace(b"=", b"")
encoded_payload_bytes = base64.urlsafe_b64encode(jwt_payload).replace(b"=", b"")

jwt_signature = hmac.digest(
    key=secret,
    msg=b".".join([encoded_header_bytes, encoded_payload_bytes]),
    digest=hashlib.sha256
)

encoded_signature_bytes = base64.urlsafe_b64encode(jwt_signature).replace(b"=", b"")

jwt_returned = (
        f"{str(encoded_header_bytes, UTF_8)}" +
        f".{str(encoded_payload_bytes, UTF_8)}" +
        f".{str(encoded_signature_bytes, UTF_8)}"
)

# Verify this token at https://jwt.io/#debugger-io
print(jwt_returned)
