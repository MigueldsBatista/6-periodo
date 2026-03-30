def eh_primo(numero: int) -> bool:
    if numero < 2:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
        
    return True

def calcular_mdc(dividend: int, divisor: int) -> int:
    while divisor != 0:
        dividend, divisor = divisor, dividend % divisor
    return dividend

def gerar_chaves():
    primo_p = 13
    primo_q = 17
    
    assert eh_primo(primo_p) and eh_primo(primo_q)
    assert primo_p != primo_q
    assert primo_p < 10000 and primo_q < 10000
    
    modulo_n = primo_p * primo_q
    
    phi_n = (primo_p - 1) * (primo_q - 1)
    
    expoente_publico = 5
    
    assert 1 < expoente_publico < phi_n and calcular_mdc(expoente_publico, phi_n) == 1
    
    expoente_privado = pow(expoente_publico, -1, phi_n)
    
    return (expoente_publico, modulo_n), (expoente_privado, modulo_n)

def cifrar_com_publica(mensagem: int, chave_publica: tuple[int, int]) -> int:
    expoente_e, modulo_n = chave_publica
    return pow(mensagem, expoente_e, modulo_n)

def decifrar_com_privada(texto_cifrado: int, chave_privada: tuple[int, int]) -> int:
    expoente_d, modulo_n = chave_privada
    return pow(texto_cifrado, expoente_d, modulo_n)

if __name__ == "__main__":
    publica, privada = gerar_chaves()
    mensagem_original = 0x41
    
    valor_cifrado = cifrar_com_publica(mensagem_original, publica)
    
    valor_decifrado = decifrar_com_privada(valor_cifrado, privada)
    
    print(f"Pub = {{{publica[0]}, {publica[1]}}}")
    print(f"Priv = {{{privada[0]}, {privada[1]}}}")
    print(f"Valor 0x41 cifrado: {valor_cifrado}")
    print(f"Valor decifrado: {hex(valor_decifrado)} ({valor_decifrado})")
    
    
    # Pub = {5, 221}
    # Priv = {77, 221}
    # Valor 0x41 cifrado: 182
    # Valor decifrado: 0x41 (65)