from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from PIL import Image
import numpy as np
import base64
import io
from ISR.models import RDN, RRDN

from .Serializers import ProcessingSerializer
from .models import ImageAI
from .models import Method


class Processing(views.APIView):
    def post(self, request, *args, **kwargs):
        model = RDN(weights='noise-cancel')
        img=request.data.get("img")
        img = (np.array(Image.open(io.BytesIO(img.file.read()))))
        processed_img_arr = model.predict(np.array(img))
        # method = Method.objects.get(id=request.data.get("method"))
        # print("FIRRRRRRRRRRRSTTTTTTTTTTTTTTTt")
        # print(method)
        # ImageAI.objects.create(method=method)
        # print("SECONDDDDDDDDDDDDDDDDDDDDDDD")
        # print(method)
        # processed_img = Image.fromarray(processed_img_arr)
        encoded_img = base64.b64encode(processed_img_arr)
        return Response(processed_img_arr, status=status.HTTP_201_CREATED)