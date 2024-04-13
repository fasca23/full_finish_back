import os
from cloud_api.models import File_tb
from cloud_api.serializers import FileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import FileResponse, HttpResponse
from django.utils import timezone

@api_view(['GET'])
@permission_classes([AllowAny])
def download_share(request, pk, **kwargs):
    
    try:
        files = File_tb.objects.get(id_uuid=pk)
        filepath = files.file_file.path
        file_type = f".{files.file_type}"
        file_name = f'{files.file_name}{file_type}'
        print(files.file_name)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                response = HttpResponse(f.read(), 
                                        content_type=file_type,
                                        charset='utf-8'
                                        )
                response['Content-Disposition'] = 'attachment; filename={0}'.format(file_name)
                return response
        
    except File_tb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download(request, pk):
    try:
        files = File_tb.objects.get(id=pk)
        filename = files.file_file.path
        if os.path.exists(filename):
            response = FileResponse(open(filename, 'rb'))
            files.last_download_time = timezone.now()
            files.save()
            return response
    except File_tb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyFiles (request):
    user = request.user   
    files = File_tb.objects.filter(user_id=user.id).order_by('-create_at')
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def FileList(request, pk):
    try:
        files = File_tb.objects.filter(user_id=pk).order_by('-create_at')
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
    except File_tb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FileDetail(request, pk):
    try:
        files = File_tb.objects.get(id=pk)
        serilizer = FileSerializer(files, many=False)
        return Response(serilizer.data)
    except File_tb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateFile(request, *args, **kwargs):
    
    user = request.user 
    data = request.data 

    files = File_tb.objects.create(
            user_id=user,
            file_file= request.FILES['file_file'],
            file_name=data['file_name'],
            description=data['description'],
            size_file=data['size_file'],
            create_at=data['create_at'],
            file_type=data['file_type']
        )
    
    serializer = FileSerializer(files, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditFile(request, pk):
    files = File_tb.objects.get(id=pk)
    serilizer = FileSerializer(instance=files, data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response({'detail':'Файл успешно обновлен!'}, status=status.HTTP_200_OK)
    return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteFile(request, pk):
    product = File_tb.objects.get(id=pk)
    filepath = product.file_file.path
    os.remove(filepath)
    product.delete()
    return Response({'detail':'Файл удален успешно!'},
                    status=status.HTTP_200_OK)