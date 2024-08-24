from rest_framework import serializers, status

from psiquepaWEB.models.models import Blog, User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'blog_content']

    def validate_blog(self):
        data = self.validated_data

    def create_blog(self, logged_user):
        user = User.objects.get(user_name=logged_user)
        blog_created = Blog.objects.create(user_id=user.psid, **self.validated_data)
        blog_id = blog_created.id
        blog_title = blog_created.title
        blog_creation_date = blog_created.creation_date
        blog_content = blog_created.blog_content
        response = dict(
            {'status': 'Blog created successfull', 'code': 'PS-0000', 'body': {
                'blog_id': blog_id,
                'blog_title': blog_title,
                'blog_creation_date': blog_creation_date,
                'blog_content': blog_content
            }}
        )
        return response

    def get_blog_by_id(self, blog_id):
        blog_returned = []
        blog_response = dict({'status': 'PS-0000', 'body': blog_returned})
        blogs = Blog.objects.filter(id=blog_id)
        if blogs.exists():
            for blog in blogs:
                data = dict(
                    {'id': blog.id, 'title': blog.title, 'blog_content': blog.blog_content, 'date': blog.creation_date,
                     'blog_image': blog.blog_image})
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
                     })
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

    def get_blogs_by_user(self, user_psid):
        blogs_of_user = []
        try:
            user_blogs = Blog.objects.filter(user_id=user_psid)
            if user_blogs.exists():
                print(user_blogs[0].__dict__.values())
                for blog in user_blogs:
                    b_id = blog.id
                    b_title = blog.title
                    b_content = blog.blog_content
                    b_date = blog.creation_date
                    blog_to_append = dict({
                        'blog_id': b_id,
                        'blog_title': b_title,
                        'blog_content': b_content,
                        'blog_date': b_date,
                    })
                    blogs_of_user.append(blog_to_append)
                response = {'status': 'User blogs', 'code': 'PS-0000', 'body': {'blogs': blogs_of_user}}

                return [response, status.HTTP_200_OK]
            return [dict([]), status.HTTP_404_NOT_FOUND]
        except User.DoesNotExist:
            return [dict({'status': 'PS-0090', 'message': 'An error has occurred'}), status.HTTP_409_CONFLICT]
