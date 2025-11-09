import numpy as np
import matplotlib.pyplot as plt

# =============================
# Signal Generators
# =============================

def unit_step(n):
    signal = np.array([1 if i >= 0 else 0 for i in n])
    plt.stem(n, signal, use_line_collection=True)
    plt.title("Unit Step Signal")
    plt.show()
    return signal

def unit_impulse(n):
    signal = np.array([1 if i == 0 else 0 for i in n])
    plt.stem(n, signal, use_line_collection=True)
    plt.title("Unit Impulse Signal")
    plt.show()
    return signal

def ramp_signal(n):
    signal = np.array([i if i >= 0 else 0 for i in n])
    plt.stem(n, signal, use_line_collection=True)
    plt.title("Ramp Signal")
    plt.show()
    return signal

def sine_wave(A, f, phi, t):
    signal = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title("Sine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def cosine_wave(A, f, phi, t):
    signal = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title("Cosine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def exponential_signal(A, a, t):
    signal = A * np.exp(a * t)
    plt.plot(t, signal)
    plt.title("Exponential Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

# =============================
# Signal Operations
# =============================

def time_shift(signal, k):
    shifted = np.roll(signal, k)
    plt.plot(shifted)
    plt.title(f"Time Shifted by {k}")
    plt.show()
    return shifted

def time_scale(signal, k):
    scaled = signal[::k]
    plt.plot(scaled)
    plt.title(f"Time Scaled by {k}")
    plt.show()
    return scaled

def signal_addition(signal1, signal2):
    result = signal1 + signal2
    plt.plot(result)
    plt.title("Signal Addition")
    plt.show()
    return result

def signal_multiplication(signal1, signal2):
    result = signal1 * signal2
    plt.plot(result)
    plt.title("Signal Multiplication")
    plt.show()
    return result

# =============================
# Main Demonstration
# =============================

if __name__ == "__main__":
    # Discrete domain
    n = np.arange(-10, 10, 1)

    # Continuous domain
    t = np.linspace(0, 1, 500)

    # 1. Generate and plot unit step & unit impulse
    u = unit_step(n)
    d = unit_impulse(n)

    # 2. Generate sine wave
    sine = sine_wave(2, 5, 0, t)

    # 3. Time shift sine wave
    shifted = time_shift(sine, 50)

    # 4. Addition of unit step and ramp
    r = ramp_signal(n)
    add_result = signal_addition(u, r)

    # 5. Multiply sine & cosine
    cosine = cosine_wave(2, 5, 0, t)
    mult_result = signal_multiplication(sine, cosine)
