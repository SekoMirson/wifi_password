import subprocess
import tkinter as tk

def show_wifi_profiles():
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
    output_label.config(text=result.stdout)
    root.update()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

def show_wifi_password():
    selected_profile = profile_entry.get()
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles', selected_profile, 'key=clear'], capture_output=True, text=True)
    output_label.config(text=result.stdout)
    root.update()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

# GUI Oluşturma
root = tk.Tk()
root.title("Wi-Fi Şifreleri")

# WiFi Profil Listesini Göster Butonu
show_profiles_button = tk.Button(root, text="Wi-Fi Profil Listesini Göster", command=show_wifi_profiles)
show_profiles_button.pack(pady=10)

# WiFi Profili Giriş Kutusu
profile_entry_label = tk.Label(root, text="Wi-Fi Profili:")
profile_entry_label.pack()
profile_entry = tk.Entry(root)
profile_entry.pack()

# WiFi Şifresini Göster Butonu
show_password_button = tk.Button(root, text="Wi-Fi Şifresini Göster", command=show_wifi_password)
show_password_button.pack(pady=5)

# Çıktı Etiketi
output_label = tk.Label(root, text="")
output_label.pack()

# Pencere boyutunu içeriğe göre otomatik ayarla
root.update()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

root.mainloop()
