# Two-Way Authentication Using Raspberry Pi

This repository contains the full implementation and documentation for our research project, published in IJNRD (Vol 8, Issue 11, Nov 2023), titled **"Two-Way Authentication Using Raspberry Pi"**.

## 🔒 Project Summary

This system integrates **biometric fingerprint authentication**, **environmental monitoring**, and **cloud-based OTP** validation using:
- Raspberry Pi (as the core controller and authenticator)
- GT511C3 Fingerprint Sensor
- DHT22 Temperature/Humidity Sensor
- Firebase for real-time OTP and storage
- MIT App Inventor-based mobile app

## 📸 Key Features

- Biometric authentication with fingerprint sensor
- Environmental validation (humidity & temperature thresholds)
- Two-way authentication: user → system, system → user
- Firebase OTP verification (Time-based OTP)
- Mobile app integration
- Real-time monitoring and remote control

## 🧠 System Architecture

Check the [hardware/wiring_diagram.png](hardware/wiring_diagram.png) for connections and the full architecture in our [paper](research/IJNRD2311374.pdf).

## 🚀 Quick Start

### Hardware Required
- Raspberry Pi 3/4
- GT511C3 Fingerprint sensor
- DHT22 Sensor
- Relay, LED, Buzzer
- Jumper wires, Breadboard

### Software Required
- Python 3
- Firebase SDK for Python (`firebase-admin`)
- MIT App Inventor (Mobile App)

### How to Run
1. Connect the hardware (see [hardware/components.md](hardware/components.md)).
2. Setup Firebase (see [cloud/firebase_structure.md](cloud/firebase_structure.md)).
3. Run `firmware/fingerprint_auth.py` on the Raspberry Pi.
4. Install the mobile APK from [`mobile_app/apk/`](mobile_app/apk/).
5. Scan the QR code (generated on Pi) using the app for TOTP setup.

## 📱 Mobile App
The mobile app enables user enrollment, OTP generation, and real-time environmental monitoring. Built using MIT App Inventor. [See Screenshots](images/screenshots/)

## 📄 Research Paper
Published in IJNRD: [Read Paper](research/IJNRD2311374.pdf)

## 📚 License
MIT License
