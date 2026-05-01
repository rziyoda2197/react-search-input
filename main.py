import time
import threading

class DebouncedAPI:
    def __init__(self, api_call, delay):
        self.api_call = api_call
        self.delay = delay
        self.lock = threading.Lock()
        self.is_calling = False

    def call_api(self, *args, **kwargs):
        with self.lock:
            if not self.is_calling:
                self.is_calling = True
                threading.Thread(target=self._call_api, args=args, kwargs=kwargs).start()

    def _call_api(self, *args, **kwargs):
        time.sleep(self.delay)
        self.api_call(*args, **kwargs)
        with self.lock:
            self.is_calling = False

def api_call(query):
    print(f"API call with query: {query}")

def main():
    debounced_api = DebouncedAPI(api_call, 1)  # 1 second delay

    def search_input_handler(query):
        debounced_api.call_api(query)

    search_input_handler("test query")

if __name__ == "__main__":
    main()
```

Bu kodda, `DebouncedAPI` klassi API chaqirishni kechiktirish uchun mo'ljallangan. `call_api` metodi API chaqirishni kechiktiradi, lekin faqatgina API chaqirish tugallanganda. `api_call` metodi API chaqirish uchun asosiy funksiya. `main` funksiyasi `DebouncedAPI` klassi va `search_input_handler` funksiyasini ishga tushiradi.
