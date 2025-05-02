# 🌱 MoodPot — *"Happy Plant, Happy You."*

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/brandinglogo.jpg" width="85" height="85">

---

## 📘 Overview

**MoodPot** adalah pot pintar berbasis Arduino yang mampu membaca kelembapan tanah dan merespons dengan ekspresi wajah melalui LED Matrix. Saat tanah kering, MoodPot menampilkan wajah sedih dan otomatis menyiram tanaman menggunakan pompa air kecil. Saat tanah cukup lembap, MoodPot menampilkan wajah senang.

Dengan pendekatan visual dan otomatisasi, MoodPot bertujuan untuk menjadikan kegiatan merawat tanaman lebih menyenangkan, komunikatif, dan mudah, terutama bagi pemula.

---

## 🎯 Objectives

- 🔍 Mendeteksi kelembapan tanah secara otomatis menggunakan sensor.
- 😊 Memberikan feedback visual (wajah senang/sedih) melalui LED Matrix.
- 💧 Menyiram tanaman secara otomatis ketika tanah kering.
- 💻 Menyediakan monitoring kelembapan secara real-time melalui UART ke komputer.

---

## 🧠 Background

Merawat tanaman sering kali menjadi tantangan, terutama bagi orang-orang sibuk atau yang belum terbiasa dengan kebutuhan dasar tanaman. Salah satu penyebab tanaman layu adalah kurangnya perhatian terhadap kelembapan tanah.

**MoodPot** memberikan solusi dengan menampilkan *"mood"* tanaman—apakah bahagia atau sedih—berdasarkan kondisi tanah, membuat pengguna lebih peduli dan terlibat.

---

## 🔧 Hardware Components

| Komponen              | Fungsi                                |
|----------------------|----------------------------------------|
| Arduino Uno          | Pengontrol utama                      |
| Sensor Kelembapan    | Membaca kadar air tanah               |
| LED Matrix (MAX7219) | Menampilkan ekspresi wajah            |
| Relay Module         | Mengendalikan pompa                   |
| Pompa DC 12V         | Menyiram tanaman otomatis             |
| Baterai 18650        | Sumber daya portabel                  |
| LED indikator        | Penanda status sistem                 |

---

## 💻 Software Tools

- [Arduino IDE](https://www.arduino.cc/en/software)
- [KiCad](https://kicad.org/)
- [Figma](https://www.figma.com/)
- [TinkerCAD](https://www.tinkercad.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

---

## 🧭 System Diagram

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/blok-sistem.png">

---

## ⚙️ Working Principle

### 🔍 Pembacaan Kelembapan
- Sensor kelembapan tanah mengirim sinyal analog ke Arduino.
- Nilai tinggi → tanah kering; nilai rendah → tanah basah.

### 🧠 Pemrosesan oleh Arduino
- Arduino membaca sensor secara berkala dan membandingkan dengan nilai *threshold*.
- Keputusan diambil untuk menyiram atau tidak.

### 😃 Feedback Visual
- Tanah basah → LED Matrix menampilkan wajah senang 😊
- Tanah kering → LED Matrix menampilkan wajah sedih 😢

### 💧 Penyiraman Otomatis
- Jika tanah kering, relay mengaktifkan pompa air.
- Setelah tanah cukup lembap, pompa dimatikan otomatis.

---

## 👨‍💻 Team — Drasoul.Tech

| NRP         | Nama Lengkap                    | Tanggung Jawab               |
|-------------|----------------------------------|------------------------------|
| 2123500003  | Audy Putra Pratama Akbar        | UI/UX Designer               |
| 2123500007  | Muhammad Faizulhaq R            | Hardware                     |
| 2123500010  | Zanuar Rachmat Yusril B.P.      | 3D Designer                  |
| 2123500014  | Ahmad Hafidz Iswananda S        | Project Manager / Hardware  |
| 2123500027  | Ingka Fitra Oemardi             | Programmer                   |

---

## 🎓 Supported by

- 👨‍🏫 Dosen Pengampu: Akhmad Hendriawan, S.T., M.T.
- 📚 Mata Kuliah: Workshop Mikrokontroler
- 🏫 Institusi: Politeknik Elektronika Negeri Surabaya (PENS)
- 🧑‍🔧 Program Studi: Teknik Elektronika

---

## ✅ Future Improvements

- [ ] Tambahkan koneksi Bluetooth untuk kontrol dari HP
- [ ] Implementasi OLED display untuk info lebih lengkap
- [ ] Desain casing 3D cetak

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Credits

Developed with 💚 by **Drasoul.Tech**  
A project to bring life, tech, and plants together 🌿
