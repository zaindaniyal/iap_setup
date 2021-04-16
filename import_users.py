import firebase_admin
from firebase_admin import auth

default_app = firebase_admin.initialize_app()

users = [
    auth.ImportUserRecord(
        uid='LJOW2K',
        email='test3@dummy.org',
        password_hash=b"$2y$12$YgVRLoRXTR89NUDR386IuuN7sZNi4LbDz.J/2U3nUFCbaqE75esbS",
        password_salt=b"salt"
    ),
]

hash_algo = auth.UserImportHash.bcrypt()
try:
    result = auth.import_users(users, hash_alg=hash_algo)
    for err in result.errors:
        print("Failed due to ", err.reason)
except Exception as e:
    print(e)