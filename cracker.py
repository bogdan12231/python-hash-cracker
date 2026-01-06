import hashlib
import time
class Wordlist:
    def __init__(self, path):
        self.path = path
    def read(self):
        with open(self.path, 'r') as file:
            for line in file:
                yield line.strip()

class Cracker(Wordlist):
    def __init__(self, path, target_hash, type_hash):
       super().__init__(path)
       self.target_hash = target_hash    
       self.type_hash = type_hash.lower()
    def brute(self):
        try:
            start_time = time.time()
            for password in self.read():
                hash_obj = hashlib.new(self.type_hash)
                hash_obj.update(password.encode("utf-8"))
                hex_d = hash_obj.hexdigest()
                if hex_d == self.target_hash:
                    end_time = time.time()
                    result_time = round(end_time - start_time, 2)
                    return f"Password is '{password}' with hash {hex_d}, it lasted {result_time} seconds" 
            return "Password didn't find"
        except Exception as e:
            return f"Erorr: {e}"

start = Cracker('Your path', 'Your hash','Type hash')
print(start.brute())