# test_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataSource
from .serializer import DataSourceSerializer

class DataSourceView(APIView):
    def get(self, request):
        data_source = DataSource()
        query = request.query_params.dict()  # Convert query params to a dictionary
        data = data_source.read(query)
        serializer = DataSourceSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DataSourceSerializer(data=request.data)
        if serializer.is_valid():
            data_source = DataSource()
            inserted_id = data_source.create(serializer.validated_data)
            return Response({"inserted_id": inserted_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        serializer = DataSourceSerializer(data=request.data)
        if serializer.is_valid():
            data_source = DataSource()
            query = {"_id": pk}  # Query by the document ID
            updated_count = data_source.update(query, serializer.validated_data)
            if updated_count:
                return Response({"updated": updated_count}, status=status.HTTP_200_OK)
            return Response({"error": "No document matched the query"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        data_source = DataSource()
        query = {"_id": pk}  # Query by the document ID
        deleted_count = data_source.delete(query)
        if deleted_count:
            return Response({"deleted": deleted_count}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "No document matched the query"}, status=status.HTTP_404_NOT_FOUND)
