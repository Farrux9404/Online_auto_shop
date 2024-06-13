from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from credit_terms.models import Credit_terms
from credit_terms.serializer import CredittermsSerializer


@api_view(['GET'])
def creditterms_list(request):
    abouts = Credit_terms.objects.all()
    serializer = CredittermsSerializer(abouts, many=True)
    serializer_url = serializer.data
    for obj_url in serializer_url:
        if obj_url.get('file'):
            obj_url['file'] = request.build_absolute_uri(obj_url['file'])
    return Response(serializer_url)


@api_view(['GET'])
def creditterms_detail(request, pk):
    try:
        about = Credit_terms.objects.get(pk=pk)
    except Credit_terms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CredittermsSerializer(about)
    return Response(serializer.data)
