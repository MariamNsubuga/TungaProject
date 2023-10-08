from rest_framework import permissions



class IsObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request,view, obj):

# Read permissions are only allowed to the owner of the note.
        if request.method in permissions.SAFE_METHODS:
            return obj.owner == request.user

        # Write permissions are only allowed to the owner of the note.
        return obj.owner == request.user