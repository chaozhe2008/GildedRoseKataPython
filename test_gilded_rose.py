# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

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

    # test3: In reality, the code will drop its quality to 0 once SellIn is below 0.
    def test_backstage_pass_incorrect_quality_after_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(52, items[0].quality)

    # test4: initializing without list will cause error
    def test_gilded_rose_single_item_without_list(self):
        items = Item("Sulfuras", 5, 80)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

if __name__ == '__main__':
    unittest.main()
