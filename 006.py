# Leia uma temperatura em graus Celsius e apresente-a convertida em Fahrenheit.

print('Digite a temperatura em Celsius:')
celsius = float(input())
fahrenheit = celsius * (9/5) + 32
print(f'A temperatura em Fahrenheit é: {fahrenheit}')