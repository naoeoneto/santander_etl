from src.extract import extract_user_ids, extract_users_by_id
from src.transform import transform_users
from src.load import load

def run_etl():
    ids = extract_user_ids('data/userids.csv')
    users = extract_users_by_id(ids)
    users = transform_users(users)
    load(users, 'data/output.json')

if __name__ == "__main__":
    run_etl()
