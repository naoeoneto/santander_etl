def generate_ai_message(user):
    return f"Olá {user['name']}, temos novidades para você!"

def transform_users(users):
    for user in users:
        message = generate_ai_message(user)
        user['news'].append({
            "description": message
        })
    return users
