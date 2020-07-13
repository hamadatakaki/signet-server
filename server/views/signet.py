from server import api
from server.models import SessionManager
from server.models.signet import Signet

import json


@api.route('/api/signet')
class SignetView:
    def on_get(self, req, resp):
        # query signet's table.
        with SessionManager() as session:
            signets = session.query(Signet).all()
        resp.media = {'signets': [s.serialize() for s in signets]}
        resp.status_code = api.status_codes.HTTP_200

    async def on_post(self, req, resp):
        data = await req.media(format='json')
        if not ('url' in data.keys() and 'position' in data.keys() and 'icon' in data.keys() and 'title' in data.keys()):
            resp.media = {'message': 'bad request','signet_id': -1}
            resp.status_code = api.status_codes.HTTP_400
            return
        title = data['title']
        if (len(title) >= len(Signet.title)):
            title = title[0:len(Signet.title)-3] + "..."
        signet = Signet(url=data['url'], icon=data['icon'], title=title, comment="", position=data['position'])
        with SessionManager() as session:
            session.add(signet)
            session.commit()
            signet_id = signet.signet_id
        resp.media = {'message': 'on post', 'signet_id': signet_id}
        resp.status_code = api.status_codes.HTTP_201

    async def on_delete(self, req, resp):
        data = await req.media(format='json')
        if 'signet_id' not in data.keys():
            resp.media =  {'message': 'bad request'}
            resp.status_code = api.status_codes.HTTP_400
            return
        with SessionManager() as session:
            session.query(Signet).filter(Signet.signet_id==data['signet_id']).delete()
            session.commit()
        resp.media = {'message': 'on delete'}
        resp.status_code = api.status_codes.HTTP_202


@api.route('/api/signet/comment')
class SignetCommentView:
    async def on_post(self, req, resp):
        data = await req.media(format='json')
        if not ('signet_id' in data.keys() and 'comment' in data.keys()):
            resp.media =  {'message': 'bad request'}
            resp.status_code = api.status_codes.HTTP_400
            return
        comment = data['comment']
        if(len(comment)>=140):
            comment = comment[0:136] + "..." + comment[-1]
        with SessionManager() as session:
            sig = session.query(Signet).get(data['signet_id'])
            sig.comment = comment
            session.commit()
        resp.media = {'message': 'on post'}
        resp.status_code = api.status_codes.HTTP_201
