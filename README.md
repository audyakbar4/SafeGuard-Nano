# 🌱 MoodPot — *"Happy Plant, Happy You."*

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/Banner.png">
<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/Team%20Member.png">

---

## 📘 Overview

🌱 MoodPot – Ketika Tanaman Bisa Bercerita Lewat Ekspresi

Pernah merasa bersalah karena lupa menyiram tanaman? Atau bingung kapan waktunya menyiram? MoodPot hadir sebagai sahabat tanaman yang bisa berbicara padamu lewat ekspresi wajah.

Bayangkan kamu pulang ke rumah setelah hari yang melelahkan. Di pojok ruangan, tanaman kesayanganmu sedang “menatap” dengan wajah sedih. Bukan karena marah—tapi karena ia haus. Tapi tenang, MoodPot sudah tahu apa yang harus dilakukan. Ia otomatis menyalakan pompa kecil dan memberi tanamanmu minuman yang dibutuhkannya.

Beberapa saat kemudian, wajahnya berubah ceria. Tanahnya lembap kembali, dan tanamanmu pun bahagia.

MoodPot bukan sekadar pot bunga. Ia adalah teman kecil yang mengingatkan kita bahwa merawat tanaman bisa menjadi pengalaman yang menyenangkan, komunikatif, dan penuh empati—bahkan untuk pemula sekalipun. Dengan sensor kelembapan tanah, ekspresi LED Matrix yang menggemaskan, dan sistem penyiraman otomatis, MoodPot menjadikan setiap interaksi kecil terasa berarti.

Karena tanaman juga punya cara untuk menyampaikan perasaannya—dan MoodPot menerjemahkannya untukmu.

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
<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/PCB%20Design/Screenshot%202025-05-16%20211504.png">
<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/PCB%20Design/Screenshot%202025-05-16%20211519.png">
<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/PCB%20Design/Screenshot%202025-05-16%20213700.png">

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
