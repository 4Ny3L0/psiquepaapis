from rest_framework import serializers

from psiquepaWEB.models.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'document_id']

    def validate_blog(self):
        data = self.validated_data

    def create_blog(self):
        blog = self.validated_data
        Blog.objects.create(**self.validated_data)
        return dict({'status': 'Created'})

    def get_blog_by_id(self):
        blogs = Blog.objects.filter(document_id='8-907-143')
        for blog in blogs:
            print(blog.title, blog.author)
        return dict({'status': 'thsh'})

    def get_all_blogs(self):
        blogs = Blog.objects.all()
        blogs_list = list()
        blogs_actual = dict({'status': 'PS-0000', 'body': blogs_list})
        for blog in blogs:
            blog_actual = dict({'title': blog.title, 'blog_content': blog.blog_content, 'date': blog.creation_date,
                                'author': blog.author})
            blogs_list.append(blog_actual)
        return blogs_actual
