from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import NotFound

from api.services import FullCardService
from api.serializers import FullCardSerializer, InsertSerializer


class FullCardViewSet(ViewSet):
    serializer_class = InsertSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, )

    def __init__(self, **kwargs):
        self.service = FullCardService()
        super().__init__(**kwargs)

    def list(self, request):
        card_number = request.query_params.get("card_number")
        data = self.service.find_card(card_number)
        if not data:
            raise NotFound("Card {number} doesn't exists.".format(number=card_number))
        
        serializer = FullCardSerializer(data, many=False)
        return Response(serializer.data)

    def create(self, request):
        serializer = InsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        insert_mode = serializer.validated_data.get("insert_mode")
        card_number = serializer.validated_data.get("card_number")
        content_file = serializer.validated_data.get("file_uploaded")
        if insert_mode=="single":
            data = self.service.insert(card_number)
        else:
            """
            Aqui, utilizei o bulk_insert para os casos de inserção em lotes,
            que é mais performático do que efetuar a persistência dos cards um de cada vez.
            Pensando em termos de escalabilidade, o método bulk_insert definido no service
            pode ser executado de forma assíncrona utilizando o Celery (não implementado).
            """
            data = self.service.bulk_insert(content_file)

        serializer = FullCardSerializer(data, many=(insert_mode=="multiple"))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
