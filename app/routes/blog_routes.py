from flask import Blueprint, request, jsonify
from ..models import BlogPost
from ..schemas import blog_post_schema, blog_posts_schema
from .. import db

bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/', methods=['POST'])
def add_blog_post():
    title = request.json['title']
    content = request.json['content']

    new_blog_post = BlogPost(title, content)
    db.session.add(new_blog_post)
    db.session.commit()

    return blog_post_schema.jsonify(new_blog_post)


@bp.route('/', methods=['GET'])
def get_blog_posts():
    all_blog_posts = BlogPost.query.all()
    result = blog_posts_schema.dump(all_blog_posts)

    return jsonify(result)


@bp.route('/<id>', methods=['GET'])
def get_blog_post(id):
    blog_post = BlogPost.query.get(id)
    return blog_post_schema.jsonify(blog_post)


@bp.route('/<id>', methods=['PUT'])
def update_blog_post(id):
    blog_post = BlogPost.query.get(id)

    title = request.json['title']
    content = request.json['content']

    blog_post.title = title
    blog_post.content = content

    db.session.commit()

    return blog_post_schema.jsonify(blog_post)


@bp.route('/<id>', methods=['DELETE'])
def delete_blog_post(id):
    blog_post = BlogPost.query.get(id)
    db.session.delete(blog_post)
    db.session.commit()

    return blog_post_schema.jsonify(blog_post)
