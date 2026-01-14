import pandas as pd
from users import data_users

def extract_user_ids(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower()
    return df

def extract_users_by_id(ids_df):
    users = []
    for user_id in ids_df['userid']:
        for user in data_users:
            if user['id'] == user_id:
                users.append(user.copy())
    return users
