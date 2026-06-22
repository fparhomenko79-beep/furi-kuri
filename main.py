def get_user_name() -> str | None:
    input_string = input().strip()
    return input_string if input_string else None

def output_welcome(user_name):
    print(f"hello {user_name}!" if user_name else f"hello nameless!")

output_welcome(get_user_name())