from Crypto.Cipher import ChaCha20


def decrypt(ciphertext: bytes, chave: str, nonce: bytes = b'12345678'):
    cipher = ChaCha20.new(key=chave.encode('utf-8'), nonce=nonce)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message

def encrypt(message: bytes, chave: str, nonce: bytes = b'12345678') -> tuple[bytes, bytes]:
    cipher = ChaCha20.new(key=chave.encode('utf-8'), nonce=nonce)
    ciphertext = cipher.encrypt(message)
    return ciphertext, cipher.nonce


message = b'Texto secreto'

chave = 'Minha chave secreta 123456'.ljust(32)[:32]

encript, nonce = encrypt(message, chave=chave, nonce=b'12345678')
print(f'Ciphertext: {encript.hex()}')
decrypted_message = decrypt(encript, chave=chave, nonce=nonce)
print(f'Decrypted message: {decrypted_message.decode("utf-8")}')

# Nonce é um meio de evitar que o mesmo texto cifrado seja gerado para a mesma mensagem e chave, garantindo que cada criptografia seja única. Ele deve ser único para cada operação de criptografia, mas não precisa ser secreto.

# EM cifra de bloco temos o conceito de IV (vetor de inicialização), que é um valor aleatório usado para garantir que a mesma mensagem cifrada com a mesma chave produza resultados diferentes. O IV é necessário para modos de operação como CBC (Cipher Block Chaining) e CFB (Cipher Feedback). Ele deve ser único e imprevisível para cada operação de criptografia, mas não precisa ser secreto.

# Conceitualmente, o nonce e o IV têm funções semelhantes, mas são usados em contextos diferentes. O nonce é mais comumente associado a cifras de fluxo, enquanto o IV é associado a cifras de bloco. Ambos são essenciais para garantir a segurança da criptografia, evitando ataques de repetição e garantindo que mensagens idênticas não resultem em textos cifrados idênticos.