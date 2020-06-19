from scrapy.item import Item, Field


class StackItem(Item):
    title = Field()
    link = Field()
    question_teaser = Field()
    user = Field()
    created = Field()
    time = Field()


class TagItem(Item):
    name = Field()



