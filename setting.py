import os

SECRET_KEY = os.getenv('SECRET_KEY', 'UBSUTv81pST8sHpkiEzEqQWW0WjV+wkTj6DvVz1o/p4=')  # openssl rand -base64 32

DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://postgres:vb12jol901@localhost:5432/postgres")

SUPERADMIN_LOGIN = os.getenv('SUPERADMIN_LOGIN', 'ADMIN')
SUPERADMIN_PASSWORD = os.getenv('SUPERADMIN_PASSWORD', 'ADMIN')
