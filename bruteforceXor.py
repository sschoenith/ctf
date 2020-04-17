import base64
import itertools
import json
import time

def xor_encrypt(data, key):
    out = []
    for i in range(len(data)):
        xor = ord(data[i]) ^ ord(key[i % len(key)])
        out.append(chr(xor))
    return "".join(out)

def decrypt(data, key):
    return json.loads(xor_encrypt(base64.b64decode(data).decode("utf-8"), key))

def bruteforce(encrypted_data, min_key_len=1, max_key_len=1):
    chars = [chr(i) for i in range(48, 123)]
    keys = []
    start_time = time.time()
    for key_len in range(1, max_key_len + 1):
        print("[{} s] Trying key length ".format(time.time() - start_time) + str(key_len))
        for product in itertools.product(chars, repeat=key_len):
            key = "".join(product)
            try:
                decrypt(encrypted_data, key)
            except:
                continue
            else:
                keys.append(key)
    print("[{} s] Completed".format(time.time() - start_time))
    return keys

def test_keys(encrypted_data, keys):
    for key in keys:
        decrypted_str = str(decrypt(encrypted_data, key))
        if decrypted_str[0] == "{" and decrypted_str[-1] == "}":
            return key

if __name__ == "__main__":
    cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
    #cookie = "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"
    keys = bruteforce(cookie, max_key_len=4)
    key = test_keys(cookie, keys)
    if key:
        print("Key: " + key)
        print("Decrypted data: " + str(decrypt(cookie, key)))
    else:
        print("No key found")
