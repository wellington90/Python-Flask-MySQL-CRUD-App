import requests
import threading

def make_requests(url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Response status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

def stress_test(url, num_threads, num_requests_per_thread):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=make_requests, args=(url, num_requests_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = "http://localhost:5000/"  # Replace with your application's URL
    num_threads = 10  # Number of concurrent threads
    num_requests_per_thread = 100  # Number of requests per thread

    stress_test(url, num_threads, num_requests_per_thread)
