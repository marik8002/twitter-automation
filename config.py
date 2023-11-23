from utils.file_system import load_file


class Config:
    ACCOUNTS = load_file("data/accounts.txt")
    PROXIES = load_file("data/proxies.txt")
    USER_AGENTS = load_file("data/user_agents.txt")

    PATH_TO_WRITE_SUSPENDED_ACCOUNTS = "data/suspended_accounts.txt"
    PATH_TO_WRITE_LOCKED_ACCOUNTS = "data/locked_accounts.txt"
    PATH_TO_WRITE_INVALID_TOKENS = "data/invalid_tokens.txt"

    THREADS = 3
    MIN_RETRIES = 1
    MAX_RETRIES = 3
    RANDOMIZE_ACCOUNTS = False

    MIN_RETRY_DELAY = 30
    MAX_RETRY_DELAY = 60

    MIN_SLEEP_BEFORE_NEXT_ACCOUNT = 1
    MAX_SLEEP_BEFORE_NEXT_ACCOUNT = 2

    MIN_SLEEP_BEFORE_NEXT_REQUEST = 3  # For automatic module only
    MAX_SLEEP_BEFORE_NEXT_REQUEST = 4  # For automatic module only


config = Config()
