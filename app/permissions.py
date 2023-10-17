from rest_framework.permissions import IsAuthenticated ,IsAdminUser,BasePermission


class WriteByAdminOnlyPermissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        if request.method == "POST" or request.method =="PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False    

        
