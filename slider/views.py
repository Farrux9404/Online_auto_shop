from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from slider.models import Slider
from slider.serializer import SliderSerializer


@api_view(['GET'])
def slider_list(request):
    abouts = Slider.objects.all()
    serializer = SliderSerializer(abouts, many=True)
    serializer_url = serializer.data
    for obj_url in serializer_url:
        if obj_url.get('image'):
            obj_url['image'] = request.build_absolute_uri(obj_url['image'])
    return Response(serializer_url)


@api_view(['GET'])
def slider_detail(request, pk):
    try:
        about = Slider.objects.get(pk=pk)
    except Slider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SliderSerializer(about)
    return Response(serializer.data)


