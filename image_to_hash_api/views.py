import hashlib
from io import BytesIO
import requests
from PIL import Image
import imagehash
from rest_framework import generics
from rest_framework.response import Response
from .models import ImageData
from .serializers import ImageDataSerializer

# Utility function to calculate MD5 and pHash
def calculate_hashes(image_url):
    response = requests.get(image_url)
    response.raise_for_status()

    # Calculate MD5
    md5_hash = hashlib.md5(response.content).hexdigest()

    # Calculate pHash
    image = Image.open(BytesIO(response.content))
    phash = str(imagehash.phash(image))

    return md5_hash, phash

# API to Create ImageData
class ImageDataCreateView(generics.CreateAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer

    def create(self, request, *args, **kwargs):
        image_url = request.data.get("image_url")
        if not image_url:
            return Response({"error": "Image URL is required"}, status=400)

        try:
            md5, phash = calculate_hashes(image_url)
            instance = ImageData.objects.create(image_url=image_url, md5_hash=md5, phash=phash)
            return Response(ImageDataSerializer(instance).data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

# List and Create API
class ImageDataListView(generics.ListCreateAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer

# Retrieve, Update, Delete API
class ImageDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer
