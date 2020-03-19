from posts.models import Like


class LikeService:

    @classmethod
    def like(cls, post_pk, user):
        like, is_created = Like.objects.get_or_create(post_id=post_pk, user=user)
        print(like, is_created)
        return like, is_created

    @classmethod
    def unlike(cls, post_pk, user):
        Like.objects.filter(post_id=post_pk, user=user).delete()

    @classmethod
    def analytics(cls, post_pk):
        return Like.objects.filter(post_id=post_pk)
