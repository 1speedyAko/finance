from django.http import HttpResponseForbidden

class ApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if not user.is_approved:
            return HttpResponseForbidden("Your account is pending approval.")
        return self.get_response(request)
