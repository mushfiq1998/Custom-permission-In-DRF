from rest_framework.permissions import BasePermission

# Define Custom permission 
class MyPermission(BasePermission):
    '''This method returns True, if the request be granted access. 
    and False otherwise. '''  
    def has_permission(self, request, view):
        '''
        # Only GET request will be accepted.
        if request.method == 'GET':
            return True
        return False'''
    
        # Only POST request will be accepted.
        if request.method == 'POST':
            return True
        return False