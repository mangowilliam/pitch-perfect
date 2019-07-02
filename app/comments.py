class Comments:

    all_comments = []

    def __init__(self, pitch_id, description, comments):
        self.pitch_id = pitch_id
        self.description = description
        self.comments = comments

    def save_review(self):
        Comments.all_comments.append(self)

    @classmethod
    def clear_reviews(cls):
        Comments.all_comments.clear()

    @classmethod
    def get_comments(cls, id):

        response = []

        for comments in cls.all_comments:
            if comments.pitch_id == id:
                response.append(comments)

        return response
