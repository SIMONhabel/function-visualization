import numpy as np
import matplotlib.pyplot as plt
import os
import functions as f

# Vytvoření složky pro obrázky, pokud neexistuje
if not os.path.exists('images'):
    os.makedirs('images')

# 4. Generování hodnot (interval -10 až 10, 1000 bodů)
x = np.linspace(-10, 10, 1000)

def save_plot(x, y, title, filename, label):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=label)
    
    # 7. Možnost C - Hledání minima a maxima pomocí NumPy
    y_min, y_max = np.min(y), np.max(y)
    x_min, x_max = x[np.argmin(y)], x[np.argmax(y)]
    
    plt.scatter([x_min, x_max], [y_min, y_max], color='red')
    plt.annotate(f'Min: {y_min:.2f}', (x_min, y_min))
    plt.annotate(f'Max: {y_max:.2f}', (x_max, y_max))

    plt.title(title)
    plt.xlabel('osa x')
    plt.ylabel('osa y')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'images/{filename}')
    plt.close()

# 5. Vykreslení a uložení jednotlivých grafů
save_plot(x, f.linear(x, 2, 3), 'Lineární funkce (2x + 3)', 'linear.png', 'f(x)=2x+3')
save_plot(x, f.quadratic(x, 1, -2, -5), 'Kvadratická funkce', 'quadratic.png', 'f(x)=x^2-2x-5')
save_plot(x, f.sine(x, 2, 1), 'Sinusoida', 'sine.png', 'f(x)=2*sin(x)')
save_plot(x, f.exponential(x, 0.5), 'Exponenciála', 'exponential.png', 'f(x)=0.5*e^x')
save_plot(x, f.absolute(x), 'Absolutní hodnota', 'absolute.png', 'f(x)=|x|')

# 6. Kombinovaný graf (3 funkce najednou)
plt.figure(figsize=(10, 6))
plt.plot(x, f.linear(x, 0.5, 2), label='Lineární', color='blue')
plt.plot(x, f.sine(x, 3, 0.5), label='Sinus', color='green')
plt.plot(x, f.absolute(x), label='Absolutní', color='purple')
plt.title('Kombinovaný graf funkcí')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-10, 10) # Omezení osy y pro přehlednost
plt.grid(True)
plt.savefig('images/multiple_functions.png')
plt.show()

print("Hotovo! Grafy najdeš ve složce 'images/'.")