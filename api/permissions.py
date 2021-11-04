from rest_framework import permissions

class ProductsAccessPermissions(permissions.BasePermission):
    message = 'Your are not allowed.'

    def has_permission(self, request, view):
        # import pdb; pdb.set_trace()
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.auth and (request.user.role==1 or request.user.role==2):
            print('auth present')
            return True


class CreateUsersPermissions(permissions.BasePermission):
    message = 'Only admins can create Users.'

    def has_permission(self, request, view):
        if request.auth and request.user.role==1:
            return True
