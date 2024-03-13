from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_no, password = None, **extra_fields):
        if not phone_no:
            raise ValueError('Phone number is required')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_no = phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, phone_no,  password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
    
        return self.create_user(phone_no, password, **extra_fields)

class UserManager(BaseUserManager):
    def create_user(self, phone_no, password=None, **extra_fields):
        if not phone_no:
            raise ValueError('Phone number is required')

        email = extra_fields.pop('email', None)  # Remove 'email' from extra_fields if present
        email = self.normalize_email(email) if email else None

        user = self.model(phone_no=phone_no, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, phone_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_no, password, **extra_fields)



# accounts\manager.py


# class UserManager(BaseUserManager):
#     def create_user(self, phone_no, password=None, **extra_fields):
#         if not extra_fields.get('email'):
#             extra_fields['email'] = ''  # Set a default email or raise an error as needed
#         email = self.normalize_email(extra_fields['email'])
#         user = self.model(phone_no=phone_no, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, phone_no, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(phone_no, password, **extra_fields)



