from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous and \
               request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_anonymous and \
               request.method in permissions.SAFE_METHODS


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and \
               request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and \
               request.method in permissions.SAFE_METHODS


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff and request.method != 'DELETE'

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff and request.method != 'DELETE'


class IsStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
