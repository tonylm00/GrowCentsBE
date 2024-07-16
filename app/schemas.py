from . import ma


class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'is_executed')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


class BlogPostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'date_created')


blog_post_schema = BlogPostSchema()
blog_posts_schema = BlogPostSchema(many=True)
