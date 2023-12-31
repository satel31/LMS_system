from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.permissions import IsOwnerPermission
from apps.users.serializers import UserSerializer, StrangerUserSerializer


class UserViewSet(ModelViewSet):
    """Viewset for User model.
       To create you need to enter email and password.
       Has different permissions for different methods and different serializers to view your data."""
    queryset = User.objects.all()
    # In case of test
    #permission_classes = [AllowAny]
    default_permission_class = [IsAuthenticated()]
    permissions = {
        'create': [AllowAny()],
        'update': [IsAuthenticated(), IsOwnerPermission()],
        'partial_update': [IsAuthenticated(), IsOwnerPermission()],
        'destroy': [IsAuthenticated(), IsOwnerPermission()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission_class)

    def get_serializer_class(self):
        try:
            if self.request.user.email == self.get_object().email:
                return UserSerializer
            return StrangerUserSerializer
        # To ignore an error in list method
        except AssertionError:
            return StrangerUserSerializer
        except AttributeError:
            return UserSerializer
