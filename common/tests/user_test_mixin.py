from common.factories import UserFactory


class UserTestBaseMixin(object):
    user = None

    def init_user(self):
        self.user = UserFactory()

    def login_user(self, user=None):
        if user is None:
            if self.user is None:
                self.init_user()
            user = self.user
        self.user = user
        self.login(user)

    def login_provider(self, user=None):
        self.login_user(user)
        if not self.user.is_provider:
            self.user.is_provider = True
            self.user.save()
