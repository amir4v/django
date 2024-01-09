#
# rest_framework.permissions
class IsNotAuthenticated(BasePermission):
    """
    Allows access only to not authenticated users.
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
#
# rest_framework.permissions
# usage: permissions.IsInGroup().dev__admin, # means: for these groups: (dev, admin)
from . import extra_path as exp
class IsInGroup(BasePermission):
    def __getattribute__(self, __name: str) -> Any:
        class Is(BasePermission):
            def has_permission(self, request, view):
                return bool(
                    request.user and
                    exp.is_member(request.user, self.group)
                )
        
        group = __name.split('__')
        
        _is = Is
        _is.group = group
        
        return _is
#
