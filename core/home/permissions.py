from rest_framework import permissions 



class Permissions_Edit_Slider(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        else:
            if obj.user_created == request.user:
                return True  
        
        