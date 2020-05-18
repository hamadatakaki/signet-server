from server import api
from server.models import SessionManager
from server.models.signet import Signet

import json


@api.route('/signets')
class SignetView:
    def on_get(self, req, resp):
        # query signet's table.
        with SessionManager() as session:
            signets = session.query(Signet).all()
        resp.media = {'signets': [s.serialize() for s in signets]}
        resp.status_code = api.status_codes.HTTP_200

    async def on_post(self, req, resp):
        data = await req.media(format='json')
        if not ('url' in data.keys() and 'position' in data.keys()):
            resp.media = {'message': 'bad request'}
            resp.status_code = api.status_codes.HTTP_301
            return
        signet = Signet(url=data['url'], icon="", title="", comment="", position=data['position'])
        with SessionManager() as session:
            session.add(signet)
            session.commit()
        # TODO: 保存したWebページのtitleとiconのURLを取ってくるバックグラウンド処理を行う.
        resp.media = {'message': 'on post'}
        resp.status_code = api.status_codes.HTTP_201

    async def on_delete(self, req, resp):
        data = await req.media(format='json')
        if 'signet_id' not in data.keys():
            resp.media =  {'message': 'bad request'}
            resp.status_code = api.status_codes.HTTP_301
            return
        with SessionManager() as session:
            session.query(Signet).filter(Signet.signet_id==data['signet_id']).delete()
            session.commit()
        resp.media = {'message': 'on delete'}
        resp.status_code = api.status_codes.HTTP_202
