from models.member_model import authenticate_member, create_member, find_member_by_login_id


def login_member(db, login_id, password):
    login_id = (login_id or "").strip()
    password = password or ""

    if not login_id or not password.strip():
        return {
            "success": False,
            "message": "Please enter your login ID and password.",
        }

    member = authenticate_member(db, login_id, password)

    if member:
        return {
            "success": True,
            "message": "Login completed.",
            "member": member,
        }

    return {
        "success": False,
        "message": "Invalid login ID or password.",
    }


def signup_member(db, login_id, password, name):
    login_id = (login_id or "").strip()
    name = (name or "").strip()
    password = password or ""

    if not login_id or not password.strip() or not name:
        return {
            "success": False,
            "message": "Please enter all required fields.",
        }

    if len(login_id) > 50 or len(password) > 50 or len(name) > 50:
        return {
            "success": False,
            "message": "Login ID, password, and name must be 50 characters or less.",
        }

    if find_member_by_login_id(db, login_id):
        return {
            "success": False,
            "message": "The login ID already exists.",
        }

    if create_member(db, login_id, password, name):
        return {
            "success": True,
            "message": "Signup completed.",
        }

    return {
        "success": False,
        "message": "Unable to create member. The login ID may already exist.",
    }
