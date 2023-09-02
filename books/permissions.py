from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        message = "permission denied, you are not the owner."
        
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user