# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

# from django.db import models


class CustomUser(AbstractUser):
    """
    Userモデルを継承したカスタムユーザーモデル
    """

    pass
