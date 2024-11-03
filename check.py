import sys
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver

def check(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    
    driver = webdriver.Chrome(options=options)
    
    with open('payloads.txt', 'r') as f:
        payloads = f.readlines()
        
    for p in payloads:
        payload = p.strip()  # Remove newline characters
        new_url = f"{url}/{payload}"
        driver.get(new_url)
        
        is_vulnerable = driver.execute_script('return Object.prototype.rdzsp')
        if is_vulnerable == 'good_hacker':
            print(f'[VULN] {new_url} [{is_vulnerable}]')
    
    driver.quit()

if __name__ == '__main__':
    # Read URLs from standard input (one per line)
    urls = [line.strip() for line in sys.stdin if line.strip()]
    
    # Use ThreadPoolExecutor for concurrency
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit the check function for each URL concurrently
        futures = [executor.submit(check, url) for url in urls]
        for future in futures:
            future.result()  # Wait for all futures to complete