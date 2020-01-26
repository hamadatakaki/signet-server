from server.models import SessionManager, Base, engine
from server.models.signet import Signet


if __name__=='__main__':
    print("--- seed! ---")
    Base.metadata.create_all(bind=engine)

    signets = [
        Signet(
            url="https://www.sig.net/new_article/?id=0324", icon="https://www.sig.net/images/2134.jpg", 
            title="ふぇ〜、フィッシュアンドチップスがこんなにたくさん...", comment="フッド姉さまが用意してくれたんだ...", position=1278
        ),
        Signet(
            url="https://onsen-musume.jp/character/iizaka_mahiro", 
            icon="https://onsen-musume.jp/wp/wp-content/themes/onsenmusume/pc/assets/img/siteinfo/favicon.ico",
            title="飯坂真尋 | 温泉むすめ公式サイト", comment="飯坂温泉行きたい", position=3456
        ),
        Signet(url="https://jellyfishrumble.net", icon="", title="jellyfishrumble.net", comment="クソサイトですまん...", position=450),
    ]

    with SessionManager() as session:
        session.bulk_save_objects(signets)
        session.commit()

    print("--- complete! ---")
