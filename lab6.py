import numpy as np
import pandas as pd

np.random.seed(0)

def generate_attack_data(attack_types):
    weights_frequencies = {
        attack: {
            'weight': np.round(np.random.uniform(0.1, 1.0), 2),
            'frequency': np.random.randint(1, 100)
        } for attack in attack_types
    }
    df_attacks = pd.DataFrame.from_dict(weights_frequencies, orient='index', columns=['weight', 'frequency'])
    df_attacks.reset_index(inplace=True)
    df_attacks.rename(columns={'index': 'Attack Type'}, inplace=True)
    df_attacks['n(Si)*wi'] = df_attacks['weight'] * df_attacks['frequency']
    return df_attacks

def print_attack_data(df_attacks, title):
    print(f"{title} Attack Data:")
    print(df_attacks)
    print(f"Total n(Si)*wi: {df_attacks['n(Si)*wi'].sum()}\n")

attack_types_linux_detailed = {
    "Service running as non-root", "Open TCP/UDP socket", "Symbolic link",
    "Weak file permission", "Service running as root", "Open remote procedure call endpoint",
    "Unpassworded account", "User id=root or group id=root account", "Setuid(setgid) root program",
    "Httpd module", "Enabled local user account", "Kernel Exploitation", "Container Escape Vulnerability", "Script enabled"
}
df_attacks_linux = generate_attack_data(attack_types_linux_detailed)
attack_types_windows = {
    "Phishing attempts", "Ransomware", "Brute force login", "Malware via email", "Drive-by download",
    "Exploiting Windows services", "Registry attack", "PowerShell attacks", "Pass-the-hash",
    "DDOS", "Man-in-the-middle", "SQL injection",
    "Cross-platform malware", "Zero-day exploit"
}
df_attacks_windows = generate_attack_data(attack_types_windows)

print_attack_data(df_attacks_linux, "Linux")
print_attack_data(df_attacks_windows, "Windows")

linux_risk = df_attacks_linux['n(Si)*wi'].sum()
windows_risk = df_attacks_windows['n(Si)*wi'].sum()

if linux_risk > windows_risk:
    print("Висновок: Операційна система Linux має вищий агрегований ризик атак у порівнянні з Windows.")
else:
    print("Висновок: Операційна система Windows має вищий агрегований ризик атак у порівнянні з Linux.")
