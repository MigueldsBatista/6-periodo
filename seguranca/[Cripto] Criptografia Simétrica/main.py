from typing import Final

from Crypto.Cipher import AES

"""
Encrypts a UTF-8 encoded string using AES encryption in GCM mode.

This module demonstrates symmetric encryption using the AES (Advanced Encryption Standard)
algorithm with GCM (Galois/Counter Mode). UTF-8 encoding is necessary because:

1. **Character Representation**: UTF-8 converts human-readable text strings into bytes,
   which is the only format that cryptographic algorithms can process.

2. **Universal Compatibility**: UTF-8 is a variable-length encoding that supports all
   Unicode characters, making it the standard for text representation.

3. **Byte Conversion Requirement**: AES cipher operations work exclusively with bytes.
   The encode() method transforms the string into its binary representation.

4. **Authenticated Encryption (GCM)**: Unlike ECB, GCM mode provides both confidentiality 
   and authenticity. It does not require padding, as it functions as a stream cipher 
   over the underlying block cipher.

Attributes:
     SECRET_KEY (bytes): A 16-byte AES encryption key (128-bit).
     DATA (bytes): The plaintext message "CESAR School" encoded as UTF-8 bytes.

The encryption process:
     1. Encodes the string to UTF-8 bytes.
     2. Initializes AES-GCM (generating a unique 16-byte Nonce automatically).
     3. Encrypts the data and generates an authentication TAG.
     4. Outputs the Nonce, Tag, and Ciphertext in hexadecimal format.
"""

# Secret key for AES encryption (must be 16, 24, or 32 bytes)
SECRET_KEY: Final = b'chave_de_16_byte'

# Data to encrypt, encoded as UTF-8 bytes
DATA = "CESAR School".encode()

# No GCM, criamos o objeto cipher. O Nonce é gerado automaticamente aqui.
encrypt_cipher = AES.new(key=SECRET_KEY, mode=AES.MODE_GCM)

# O GCM não usa padding. O método encrypt_and_digest retorna o dado cifrado e a tag.
encrypted_data, tag = encrypt_cipher.encrypt_and_digest(DATA)

# Para decriptar, o receptor precisará do NONCE, da TAG e do dado encriptado.
print(f"NONCE:      {encrypt_cipher.nonce.hex()}")
print(f"TAG:        {tag.hex()}")
print(f"ENCRYPTED:  {encrypted_data.hex()}")

decrypted_data = encrypt_cipher.decrypt(encrypted_data)



"""
Decrypts a ciphertext using AES-GCM and verifies its authenticity.

The decryption process in GCM mode requires:
1. **Nonce**: The exact same unique number used during encryption.
2. **Tag**: The Message Authentication Code (MAC) to verify integrity.
3. **Ciphertext**: The actual encrypted bytes.

The verify() step is implicit in decrypt_and_verify. If the data was 
tampered with, the process will fail, ensuring the message is authentic.
"""

try:
    decrypt_cipher = AES.new(key=SECRET_KEY, mode=AES.MODE_GCM, nonce=encrypt_cipher.nonce)

    # Se a TAG for inválida, ele levanta um ValueError aqui
    decrypted_data = decrypt_cipher.decrypt_and_verify(
        ciphertext=encrypted_data,
        received_mac_tag=tag
    )

    original_text = decrypted_data.decode()

    print(f"DECRYPTED SUCCESS: {original_text}")

except ValueError:
    print("ERRO: Tag de autenticação inválida! Os dados foram corrompidos ou a chave está errada.")
except Exception as e:
    print(f"ERRO inesperado: {e}")