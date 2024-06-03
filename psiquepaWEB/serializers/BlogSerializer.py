from rest_framework import serializers, status

from psiquepaWEB.models.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'document_id', 'blog_content']

    def validate_blog(self):
        data = self.validated_data

    def create_blog(self):
        blog = self.validated_data
        Blog.objects.create(**self.validated_data)
        return dict({'status': 'Created'})

    def get_blog_by_id(self, blog_id):
        blog_returned = []
        blog_response = dict({'status': 'PS-0000', 'body': blog_returned})
        blogs = Blog.objects.filter(id=blog_id)
        if blogs.exists():
            for blog in blogs:
                data = dict(
                    {'id': blog.id, 'title': blog.title, 'blog_content': blog.blog_content, 'date': blog.creation_date,
                     'author': blog.author, 'blog_image': blog.blog_image})
                blog_returned.append(data)
            return [blog_response, status.HTTP_200_OK]
        empty_response = blog_response.copy()
        empty_response['status'] = 'PS-0020'
        empty_response['message'] = f'No blogs with the id: {blog_id}'
        return [empty_response, status.HTTP_404_NOT_FOUND]

    def get_all_blogs(self):
        blogs = Blog.objects.all()
        blogs_list = list()
        blogs_actual = dict({'status': 'PS-0000', 'body': blogs_list})
        if blogs.exists():
            for blog in blogs:
                blog_actual = dict(
                    {'id': blog.id, 'title': blog.title, 'blog_content': blog.blog_content, 'date': blog.creation_date,
                     'author': blog.author})
                blogs_list.append(blog_actual)
            return [blogs_actual, status.HTTP_200_OK]
        empty_response = blogs_actual.copy()
        empty_response['status'] = 'PS-0020'
        empty_response['message'] = 'No Blogs yet'
        return [empty_response, status.HTTP_404_NOT_FOUND]

    def delete_blog_by_id(self, blog_id):
        blog = Blog.objects.filter(id=blog_id)
        if blog.exists():
            blog.delete()
            return [dict({'status': 'PS-0000', 'message': 'Blog deleted successfully'}), status.HTTP_200_OK]
        return [dict({'status': 'PS-0090', 'message': 'An error has occurred'}), status.HTTP_409_CONFLICT]
