# 🌱 MoodPot — *"Happy Plant, Happy You."*

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/Banner.png">
<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/Team%20Member.png">

---

## 🎬 Commercial Video

[![Watch the demo](https://img.youtube.com/vi/MjPV3MSSsJY/0.jpg)](https://youtu.be/MjPV3MSSsJY)

## Read The Book Now

[![Buka Buku](https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/Gambar/coverbook.jpg)](https://drive.google.com/file/d/1HuYGjgtTOYwcRgPvUPsH1EMrSk2Qgu1x/view?usp=drive_link)

## 🎬 Demo Video Project

[![Watch the demo](https://img.youtube.com/vi/0xyM6YmwgGI/0.jpg)](https://youtu.be/0xyM6YmwgGI)

## 📘 Overview

🌱 MoodPot – When Plants Can Speak Through Expressions

Have you ever felt guilty for forgetting to water your plants? Or unsure when to water them? MoodPot is your plant's little companion that speaks to you through facial expressions.

Imagine coming home after a long day. In the corner, your beloved plant is "staring" at you with a sad face. Not because it's mad—but because it's thirsty. Don't worry, MoodPot knows exactly what to do. It automatically activates a small pump and gives your plant the drink it needs.

Moments later, its face changes to a happy smile. The soil is moist again, and your plant is happy.

MoodPot is more than a flowerpot. It's a little friend that reminds us that taking care of plants can be fun, engaging, and full of empathy—even for beginners. Equipped with a soil moisture sensor, an adorable LED matrix face, and an automatic watering system, MoodPot turns simple interactions into meaningful experiences.

Because plants have feelings too—and MoodPot helps express them.

---

## 🎯 Objectives

* 🔍 Automatically detect soil moisture using sensors.
* 😊 Provide visual feedback (happy/neutral/sad faces) via LED Matrix.
* 💧 Automatically water plants when the soil is dry.
* 💻 Display real-time soil moisture data via UART to a computer.

---

## 🧠 Background

Caring for plants can be a challenge, especially for busy people or those unfamiliar with plant needs. One common cause of wilting is lack of soil moisture.

**MoodPot** offers a solution by displaying the plant's "mood"—whether it's happy, okay, or sad—based on the soil condition, encouraging users to be more attentive and involved.

---

## 🖼️ Presentation Preview

[![View Presentation](https://img.shields.io/badge/View-Presentation-blue?style=for-the-badge\&logo=canva)](https://www.canva.com/design/DAGlx_uOutM/ZLQWICtEFxtw9B-cfxxKvQ/edit?utm_content=DAGlx_uOutM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

> Click the button above to view the full presentation on Canva.

---

## 🧾 Presentation Table of Contents

1. Background & Problem Statement
2. MoodPot Concept
3. Components Used
4. System Diagram
5. Demo & Visualization
6. Benefits and Future Development

---

## 🔧 Hardware Components

| Component             | Function                       |
| --------------------- | ------------------------------ |
| 🧠 Arduino Nano          | Main controller                |
| 🌱 Soil Moisture Sensor  | Reads soil moisture levels     |
| 😃 LED Matrix (MAX7219)  | Displays facial expressions    |
| 🔌 Relay Module          | Controls the pump              |
| 💦 5V DC Pump            | Automatically waters the plant |
| 🔋 18650 2S Battery Pack | Portable power source          |

---

## 💻 Software Tools

* [Arduino IDE](https://www.arduino.cc/en/software)
* [KiCad](https://kicad.org/)
* [Figma](https://www.figma.com/)
* [TinkerCAD](https://www.tinkercad.com/)
* [Thingiverse](https://www.thingiverse.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

---

## 🧭 System Diagram

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/Assets/Diagram%20init.png">

## Schematic

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/PCB%20Design/Schematic.png">

## Layout

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/PCB%20Design/Layout.png">

## 3D PCB

<img src="https://github.com/audyakbar4/SafeGuard-Nano/blob/main/PCB%20Design/3D%20Viewer%20PCB.png">

---

## 💡 Project Simulation

[![Wokwi Simulation](https://img.shields.io/badge/Wokwi-Simulation-gray?logo=arduino)](https://wokwi.com/projects/431903301521434625)

🔗 **Wokwi Project Link**
[https://wokwi.com/projects/431903301521434625](https://wokwi.com/projects/431903301521434625)

📁 **Project Documentation (Google Drive)**
[https://drive.google.com/drive/folders/1F2bn2rR7vp30GGokSu8VewNVUbs7nqkA?usp=drive\_link](https://drive.google.com/drive/folders/1F2bn2rR7vp30GGokSu8VewNVUbs7nqkA?usp=drive_link)

## 📄 3D Design

📁 **3D Design Tutorial (Google Drive)**
[👉 Click here to open the Google Drive folder](https://drive.google.com/drive/folders/1GnPXin400DgNMjtPwBu-FTDF2DJWISpB?usp=drive_link)

🔗 **3D Design Vol 1**
[https://www.thingiverse.com/thing:7030558](https://www.thingiverse.com/thing:7030558)

🔗 **3D Design Vol 2**
[https://www.thingiverse.com/thing:7048423](https://www.thingiverse.com/thing:7048423)

🔗 **Desain 3D Vol **  
[https://www.thingiverse.com/thing:7050436](https://www.thingiverse.com/thing:7050436)

---

## ⚙️ Working Principle

### 🔍 Soil Moisture Reading

* The soil sensor sends an analog signal to the Arduino.
* High value → dry soil; low value → moist soil.

### 🧠 Arduino Processing

* Arduino reads the sensor periodically and compares it with a set threshold.
* It decides whether watering is needed.

### 😃 Visual Feedback

* Moist soil   → LED matrix shows a happy face 😊
* Medium soil  → LED matrix shows a neutral face 😐
* Dry soil     → LED matrix shows a sad face 😢

### 💧 Automatic Watering

* If the soil is dry, the relay activates the water pump.
* Once the soil is moist enough, the pump turns off automatically.

---

## 🚀 Quick Start

MoodPot is delivered as a plug-and-play device. Here's how to get started:

### 🪴 MoodPot Usage Steps:

1. **Fill the Water Tank**
   Prepare a container, fill it with water, and place the water pump inside.

2. **Power It Up**
   Connect MoodPot to a power source using a USB cable or the built-in 2S 18650 battery.

3. **Insert the Sensor into Soil**
   Make sure the soil sensor is properly inserted into the plant pot.

4. **Observe Facial Expressions**
   MoodPot will turn on and show expressions:

   * 😊 Happy → Moist soil, no need to water
   * 😐 Neutral → Soil drying, preparing to water
   * 😢 Sad → Dry soil, pump will water automatically

5. **Done!**
   MoodPot will operate automatically 24/7 with no manual configuration.

> 💡 Tip: Check the water tank every few days to ensure it's not empty.

---

## 👨‍💻 Team — Drasoul.Tech

| ID         | Full Name                  | Responsibility             |
| ---------- | -------------------------- | -------------------------- |
| 2123500003 | Audy Putra Pratama Akbar   | UI/UX Designer             |
| 2123500007 | Muhammad Faizulhaq R       | Hardware                   |
| 2123500010 | Zanuar Rachmat Yusril B.P. | 3D Designer                |
| 2123500014 | Ahmad Hafidz Iswananda S   | Project Manager / Hardware |
| 2123500027 | Ingka Fitra Oemardi        | Programmer                 |

---

## 🌍 Showcase

* 📢 Presented at **PENS Microcontroller Workshop 2025**
* 🌟 Featured in a live demo by supervising lecturer
* 👨‍🏫 Received positive feedback from faculty and peers

📸 Event Documentation:
[👉 Click here to view](https://drive.google.com/drive/folder-link)

---

## 🎓 Supported by

* 👨‍🏫 Supervisor: Akhmad Hendriawan, S.T., M.T.
* 📚 Course: Microcontroller Workshop
* 🏫 Institution: Politeknik Elektronika Negeri Surabaya (PENS)
* 🧑‍🔧 Program: Electronics Engineering

---

## ✅ Future Improvements

* [ ] Add Bluetooth for smartphone control
* [ ] Add OLED display for detailed information
* [ ] 3D-printed enclosure design

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Credits

Developed with 💚 by **Drasoul.Tech**
A project to bring life, tech, and plants together 🌿

## 📫 Contact Information

For inquiries about this project — collaborations, technical questions, or professional opportunities — feel free to reach out via email:

**📧 Email:** [yourname@example.com](mailto:yourname@example.com)

I aim to respond within 1–2 business days. Please include the project name in your subject line for faster response.

