from pathlib import Path

def rotate_right(b, i):
    """Rotate byte b right by i % 8 bits."""
    i %= 8
    return ((b >> i) | ((b << (8 - i)) & 0xFF)) & 0xFF

def rotate_left(b, i):
    """Rotate byte b left by i % 8 bits."""
    i %= 8
    return (((b << i) & 0xFF) | (b >> (8 - i))) & 0xFF

def decrypt_quixorte(enc_path, out_path):
    enc = bytearray(Path(enc_path).read_bytes())
    n = len(enc)
    klen = 8

    # Known PNG file header (first 8 bytes)
    png_header = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

    # Step 1. Compute rotated header R[p] = rotate_right(flag[p], p)
    R = [rotate_right(b, i) for i, b in enumerate(png_header)]

    # Step 2. Recover key bytes iteratively
    key = [0] * klen
    xor_prefix = 0
    for p in range(klen):
        key[p] = R[p] ^ enc[p] ^ xor_prefix
        xor_prefix ^= key[p]

    key_bytes = bytes(key)
    print("[+] Recovered key:", key_bytes.hex())

    # Step 3. Reverse the sliding XOR
    dec = bytearray(enc)
    for i in range(n - klen, -1, -1):
        for j in range(klen):
            dec[i + j] ^= key_bytes[j]

    # Step 4. Unrotate each byte
    flag = bytearray(rotate_left(b, i) for i, b in enumerate(dec))

    # Step 5. Verify PNG header and save output
    Path(out_path).write_bytes(flag)
    if flag[:8] == png_header:
        print("[+] Decryption successful, PNG header verified.")
    else:
        print("[!] Warning: PNG header mismatch.")
    print(f"[+] Decrypted file saved as: {out_path}")

if __name__ == "__main__":
    decrypt_quixorte("quote.png.enc", "quote_decrypted.png")
