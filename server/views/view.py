from server import api
from server.models import SessionManager
from server.models.signet import Signet

import json


@api.route('/signets')
class SignetView:
    def on_get(self, req, resp):
        resp.media = {'message': 'on_get'}
        resp.status_code = api.status_codes.HTTP_200

    async def on_post(self, req, resp):
        data = await req.media(format='json')
        print(data)
        resp.media = {'message': 'on_post'}
        resp.status_code = api.status_codes.HTTP_201

    async def on_delete(self, req, resp):
        data = await req.media(format='json')
        print(data)
        resp.media = {'message': 'on_delete'}
        resp.status_code = api.status_codes.HTTP_202
