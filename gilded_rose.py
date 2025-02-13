# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class UpdateStrategy:
    def update(self, item: Item):
        raise NotImplementedError("Subclasses must implement update()")


class NormalStrategy(UpdateStrategy):
    def update(self, item: Item):
        decrement = 1 if item.sell_in >= 0 else 2
        item.quality = max(item.quality - decrement, 0)
        item.sell_in -= 1


class AgedBrieStrategy(UpdateStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1


class BackstagePassStrategy(UpdateStrategy):
    def update(self, item: Item):
        if item.sell_in < 0:
            item.quality = 0
        else:
            if item.sell_in > 10:
                increment = 1
            elif item.sell_in >= 6:
                increment = 2
            else:
                increment = 3
            item.quality = min(50, item.quality + increment)
        item.sell_in -= 1


class SulfurasStrategy(UpdateStrategy):
    def update(self, item: Item):
        pass  # Legendary item: no changes at all


class ConjuredStrategy(UpdateStrategy):
    def update(self, item: Item):
        decrement = 2 if item.sell_in >= 0 else 4
        item.quality = max(item.quality - decrement, 0)
        item.sell_in -= 1


def get_strategy(item: Item) -> UpdateStrategy:
    if item.name == "Aged Brie":
        return AgedBrieStrategy()
    elif item.name.startswith("Backstage passes"):
        return BackstagePassStrategy()
    elif item.name.startswith("Sulfuras"):
        return SulfurasStrategy()
    elif item.name.startswith("Conjured"):
        return ConjuredStrategy()
    else:
        return NormalStrategy()

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = get_strategy(item)
            strategy.update(item)

