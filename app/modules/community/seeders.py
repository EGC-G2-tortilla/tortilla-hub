from core.seeders.BaseSeeder import BaseSeeder
from app.modules.community.models import Community
from app.modules.auth.models import User
from app.modules.dataset.models import DataSet


class CommunitySeeder(BaseSeeder):

    def run(self):

        user = User.query.filter_by(email='user3@example.com').first()

        if not user:
            raise Exception("User not found. Please seed users first.")

        community = Community(name="Super Important Community", url="https://IMPORTANTimportant.com",
                              description="Very very important because this community was " +
                              "created by very important people in a very important place in a very important date.")

        community.admin = user.id
        community.members.append(user)

        data = [
            community
        ]

        self.seed(data)

        dataset = DataSet.query.filter_by(user_id=user.id).first()

        if not dataset:
            raise Exception("Dataset not found. Please seed users first.")

        dataset.community_id = community.id

        self.seed([dataset])
