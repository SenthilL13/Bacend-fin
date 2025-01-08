from connection import py_connection


def fn_signup_user(request):
    rval = 0
    msg = "Something went wrong!"
    try:
        username = request.get("username")
        password = request.get("password")
        email = request.get("email")
        check_query = f"SELECT id FROM users WHERE username = '{username}' OR email_id = '{email}'"
        existing_user = py_connection.get_result(check_query)
        if existing_user:
            return {"rval": rval, "msg": "Username or email already exists."}
        signup_query = """
        INSERT INTO users (username, email_id, password) 
        VALUES (?, ?, ?)
        """
        result = py_connection.put_result(signup_query, (username, password, email))
        msg = "Signup successful!" if result > 0 else "Signup failed."
        rval = 1 if result > 0 else 0
        return {"rval": rval, "msg": msg}
    except Exception as e:
        print(f"Error during signup: {e}")
        return {"rval": rval, "msg": msg}


def fn_login_user(request):
    rval = 0
    msg = "Something went wrong!"
    try:
        username = request.get("username")
        password = request.get("password")
        login_query = f" SELECT user_id, username, isadmin FROM users where username = '{username}' AND " \
                      f"password = '{password}';"
        print(login_query)
        result = py_connection.get_result(login_query)
        if result:
            rval = 1
            msg = "success"
            return {
                "rval": rval,
                "msg": msg,
                "user_id": result[0][0],
                "isadmin": result[0][2]
            }
        else:
            return {"msg": "Invalid username or password", "rval": rval}
    except Exception as e:
        print("login " + str(e))
        return {"rval": rval, "msg": msg, "user_id": "", "username": "", "email": "",
                "created_at": ""}
