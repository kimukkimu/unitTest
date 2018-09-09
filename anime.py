class Anime:
    """
    お気に入りのアニメを登録する
    """

    def __init__(self):
        self.favorite_animes = []

    def favorite(self, anime):
        """
        アニメをお気に入り登録する
        :param str anime:お気に入り登録するアニメのタイトル
        """

        if anime not in self.favorite_animes:
            self.favorite_animes.append(anime)

        return self

    def least_favorite(self, anime):
        """
        アニメをお気に入りから削除する
        未登録のアニメだった場合は例外を送出して呼び出し元へ知らせる
        :param anime: お気に入りから削除するアニメのタイトル
        :return:
        """

        if anime in self.favorite_animes:
            self.favorite_animes.remove(anime)
        else:
            raise Exception('指定したアニメはお気に入りリストに存在しません')

        return self