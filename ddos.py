import requests
from concurrent.futures import ThreadPoolExecutor

url = "https://www.uznexnft.com/"
num_threads = 9999999999999999999999999

def send_request():
    try:
        response = requests.get(url)
        print(f'Status code: {response.status_code}')
    except requests.RequestException as e:
        print(f'Request error: {e}')

# Use ThreadPoolExecutor for better management of threads
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(send_request) for _ in range(num_threads)]
    for future in futures:
        try:
            future.result()  # Ensures exceptions in threads are raised
        except Exception as e:
            print(f'Unhandled error: {e}')

print('Load test completed.')
