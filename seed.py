from server.models import SessionManager, Base, engine
from server.models.signet import Signet


if __name__=='__main__':
    print("--- seed! ---")
    Base.metadata.create_all(bind=engine)

    signets = [
        Signet(url="https://www.sig.net/new_article/?id=0324", position=1278),
        Signet(url="https://onsen-musume.jp/character/iizaka_mahiro", position=3456),
        Signet(url="https://jellyfishrumble.net", position=450),
    ]

    with SessionManager() as session:
        session.bulk_save_objects(signets)
        session.commit()

    print("--- complete! ---")
