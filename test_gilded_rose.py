# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # test1: logical error for aged brie
    def test_aged_brie_quality_increase_after_sell_in(self):
        items = [Item("Aged Brie", -1, 10)]  # SellIn is 0 (past sell-by date)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)  # quality should increase by 1 not 2

    # test2: conjured items should degrade twice as fast
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 5, 10)]  # Conjured item
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    # test3: Cap at 50
    def test_backstage_pass_incorrect_quality_after_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # test4: Normal product
    def test_normal_strategy(self):
        items = [Item("Book", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(29, items[0].quality)


if __name__ == '__main__':
    unittest.main()
