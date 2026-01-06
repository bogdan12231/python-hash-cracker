import hashlib
def make_hash():
    type_hash = str(input("Write type your hash: "))
    hash_obj = hashlib.new(type_hash)
    text = "text which you want hash"
    hash_obj.update(text.encode("utf-8"))
    hex_d = hash_obj.hexdigest()
    return f"Your hash is {hex_d}"

print(make_hash())