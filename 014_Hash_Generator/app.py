import hashlib

def generate_hash(text, algorithm='sha256'):
    hash_function = getattr(hashlib, algorithm)
    hashed = hash_function(text.encode()).hexdigest()
    return hashed

def main():
    print("=== Hash Generator ===")
    text = input("Enter the text to hash: ")

    print("\nSelect hashing algorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")
    choice = input("Your choice (1/2/3/4): ")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512"
    }

    selected_algo = algorithms.get(choice, "sha256")
    result = generate_hash(text, selected_algo)

    print(f"\nHashed using {selected_algo.upper()}:")
    print(result)

if __name__ == "__main__":
    main()