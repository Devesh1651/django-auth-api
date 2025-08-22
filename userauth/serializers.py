from rest_framework import serializers
from .models import User
from .utils import generate_otp, send_otp_email, redis_client

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'email','username', 'first_name', 'last_name', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        otp = generate_otp()
        send_otp_email(user.email, otp)

        user._generated_otp = otp  # For Postman response
        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if hasattr(instance, '_generated_otp'):
            rep['otp'] = instance._generated_otp  # For demo/testing
        return rep


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        if user.is_verified:
            raise serializers.ValidationError("User is already verified.")

        stored_otp = redis_client.get(f"otp:{user.email}")
        if not stored_otp or stored_otp != data['otp']:
            raise serializers.ValidationError("Invalid or expired OTP.")

        user.is_verified = True
        user.save()
        redis_client.delete(f"otp:{user.email}")
        return data


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self):
        email = self.validated_data['email']
        otp = generate_otp()
        send_otp_email(email, otp)


class PasswordResetVerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        stored_otp = redis_client.get(f"otp:{data['email']}")
        if not stored_otp or stored_otp != data['otp']:
            raise serializers.ValidationError("Invalid or expired OTP.")
        return data


class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(min_length=6)

    def validate(self, data):
        try:
            User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        return data

    def save(self):
        email = self.validated_data['email']
        new_password = self.validated_data['new_password']
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
