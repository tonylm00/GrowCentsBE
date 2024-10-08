from . import ma


class BlogPostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'date_created')


blog_post_schema = BlogPostSchema()
blog_posts_schema = BlogPostSchema(many=True)


class TradeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'ticker', 'company', 'unit_price', 'quantity', 'date', 'type')


trade_schema = TradeSchema()
trades_schema = TradeSchema(many=True)
