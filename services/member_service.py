from werkzeug.security import check_password_hash, generate_password_hash

from models.member_model import MemberModel


class MemberService:
    """Business logic for member signup and login."""

    def __init__(self, database):
        self.member_model = MemberModel(database)

    def signup(self, user_id, password, name):
        user_id = user_id.strip()
        name = name.strip()

        if not user_id or not password or not name:
            return False, "아이디, 비밀번호, 이름을 모두 입력해주세요.", None

        if self.member_model.find_by_user_id(user_id):
            return False, "이미 사용 중인 아이디입니다.", None

        password_hash = generate_password_hash(password)
        member_id = self.member_model.create_member(user_id, password_hash, name)

        if member_id is None:
            return False, "회원가입 중 오류가 발생했습니다.", None

        member = {
            "id": member_id,
            "user_id": user_id,
            "name": name,
        }
        return True, "회원가입이 완료되었습니다.", member

    def login(self, user_id, password):
        user_id = user_id.strip()

        if not user_id or not password:
            return False, "아이디와 비밀번호를 입력해주세요.", None

        member = self.member_model.find_by_user_id(user_id)

        if member is None or not check_password_hash(member["password"], password):
            return False, "아이디 또는 비밀번호가 올바르지 않습니다.", None

        if member["activation_type"] != 1:
            return False, "비활성화된 회원입니다.", None

        return True, "로그인되었습니다.", member
