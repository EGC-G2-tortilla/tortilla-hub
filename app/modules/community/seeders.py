from core.seeders.BaseSeeder import BaseSeeder
from app.modules.community.models import Community


class CommunitySeeder(BaseSeeder):

    def run(self):

        data = [
            Community(name="Super Important Community", url="https://IMPORTANTimportant.com",
                      description="Very very important because this community was " +
                      "created by very important people in a very important place in a very important date.")
        ]

        self.seed(data)
