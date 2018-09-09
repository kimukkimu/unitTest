import unittest
from anime import Anime

class AnimeTest(unittest.TestCase):

    "easy_to_use_anime_instanceで生成したときのアニメのリスト"
    easy_to_use_anime_titles = ['ポケモン', 'ドラえもん', 'アンパンマン']

    def easy_to_use_anime_instance(self):
        """
        テストで使いやすいように初期データを登録したアニメインスタンスを返す
        :return: Anime
        """
        anime = Anime()
        for easy_title in self.easy_to_use_anime_titles:
            anime.favorite(easy_title)
        return anime

    def test_single_call_favorite(self):
        """
        favoriteメソッドを１回だけコールして正常に登録できたかテストする
        """
        anime_title = '日常'
        anime = Anime()
        anime.favorite(anime_title)

        self.assertEqual(anime_title, anime.favorite_animes[0])

    def test_multiple_call_favorite(self):
        """
        favoriteメソッドを複数回コールして正常に登録できたかテストする
        """
        anime = self.easy_to_use_anime_instance()
        self.assertEqual(self.easy_to_use_anime_titles, anime.favorite_animes)

    def test_favorite_send_duplication_anime(self):
        """
        お気に入りアニメタイトルを重複して登録されないかテストする
        """
        anime_title = '日常'
        anime = Anime()
        anime.favorite(anime_title)
        anime.favorite(anime_title)

        self.assertEqual(len(anime.favorite_animes), 1)
        self.assertEqual(anime_title, anime.favorite_animes[0])

    def test_least_favorite(self):
        """
        お気に入りアニメリストから指定のアニメが正常に消えるかテスト
        easy_to_use_anime_instance を使って初期データを用意している
        """
        anime =self.easy_to_use_anime_instance()
        anime.least_favorite('ポケモン')

        self.assertEqual(len(anime.favorite_animes), 2)
        self.assertEqual(['ドラえもん', 'アンパンマン'], anime.favorite_animes)

    def test_least_favorite_with_nodata(self):
        """
        お気に入りアニメリストに存在しないアニメを削除しようとしたときに例外が送出されるかテスト
        """
        anime =Anime()
        with self.assertRaises(Exception) as e:
            anime.least_favorite('ワンピース')

        self.assertEqual('指定したアニメはお気に入りリストに存在しません', e.exception.args[0])
