# rest_framework.permissions
class IsNotAuthenticated(BasePermission):
    """
    Allows access only to not authenticated users.
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
#
