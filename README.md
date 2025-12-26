# Hybrid Cryptographic Steganography for Secure  Data Transmission
   This project delivers a dual-layer security solution by combining strong cryptographic encryption with invisible image-based steganography, ensuring confidential, tamper-proof, and undetectable data transmission over open networks

## About:

This project focuses on developing a secure and intelligent system for confidential data transmission by integrating cryptography and steganography into a single hybrid framework. The system first encrypts sensitive text data using the Fernet authenticated encryption scheme, which combines AES-128 encryption with HMAC-SHA256 to ensure confidentiality and integrity. The encrypted data is then invisibly embedded into digital images using the Least Significant Bit (LSB) steganography technique, making the presence of secret communication undetectable to unauthorized users.

The project emphasizes high security, data integrity, and imperceptibility while maintaining image quality, validated using Peak Signal-to-Noise Ratio (PSNR) analysis. A user-friendly Streamlit-based interface enables easy embedding, extraction, encryption, and decryption without requiring advanced technical knowledge. This hybrid approach provides a practical, reliable, and efficient solution for secure communication, suitable for applications such as defense communication, cloud data protection, digital watermarking, and confidential information exchange.

## Features:

1) Dual-layer security combining encryption and steganography

2) Strong Fernet encryption (AES-128 with HMAC-SHA256) for data integrity

3) Invisible LSB-based image embedding with minimal visual distortion

4) High image quality maintained and verified using PSNR analysis

5) Tamper-proof data extraction with accurate message recovery

6) Simple and user-friendly Streamlit interface for secure communication

## Requirements:

**Operating System:** Requires a 64-bit OS such as Windows 10/11 or Ubuntu Linux to ensure compatibility with Python libraries, cryptographic modules, and image processing frameworks.

**Development Environment:** Python 3.10 or later is required for implementing the cryptographic, steganographic, and user interface modules.

**Cryptographic Frameworks:** Cryptography library (Fernet) is essential for implementing AES-128 encryption with HMAC-SHA256 based authenticated security.

**Image Processing Libraries:** Pillow and NumPy are required for image handling, pixel-level manipulation, and LSB-based data embedding and extraction.

**Web Interface Framework:** Streamlit is used to develop a simple, interactive, and user-friendly web-based interface for secure data hiding and retrieval.

**IDE & Tools:** Visual Studio Code or any compatible Python IDE is recommended for coding, debugging, and project management.

## System Architecture:

The system securely encrypts user data and invisibly embeds it into digital images using a hybrid cryptographic–steganographic approach.
It enables reliable extraction, decryption, and quality analysis through a user-friendly interface while preserving image integrity.

<img width="550" height="337" alt="Screenshot 2025-12-26 101515" src="https://github.com/user-attachments/assets/2e7babe1-7bab-44e1-bcb6-1d2abfc0e9c8" />

## Output:

![WhatsApp Image 2025-12-22 at 11 06 52 PM](https://github.com/user-attachments/assets/08dc3d9a-7b18-4b54-9daa-55a59dd23c5a)

![WhatsApp Image 2025-12-22 at 11 06 53 PM (1)](https://github.com/user-attachments/assets/ddc1b407-6103-401d-b29a-8f54ed9c3e4d)

![WhatsApp Image 2025-12-22 at 11 06 53 PM](https://github.com/user-attachments/assets/ce3b9ed0-6392-4e5f-8a57-02bb8574d2da)

![WhatsApp Image 2025-12-22 at 11 06 54 PM](https://github.com/user-attachments/assets/a5d0ea38-ca07-44bf-ab93-afde1c080266)

## Results and Impact:

The system successfully achieved secure and invisible data transmission with 100% accurate message extraction and no data loss, while maintaining high image quality with PSNR values above 45 dB. Tamper detection using HMAC ensured strong data integrity, preventing unauthorized modifications.

The project demonstrates a practical, user-friendly security solution that enhances confidentiality and stealth in digital communication. Its hybrid approach significantly improves resistance to interception and analysis, making it impactful for real-world applications such as secure messaging, cloud data protection, and digital watermarking.

## Articles published / References:

Zaidan, B. B., Zaidan, A. A., & Alanazi, H. O., A Novel Approach for High Secure Data Hiding Using Cryptography and Steganography, International Journal of Computer Science, 2010.

Roy, S., & Bora, S. D., Hybrid Image Cryptography and Steganography Method for Data Security, IEEE Conference Proceedings, 2023.

Vineela Reddy, M., & Anudeep Reddy, G., Hybrid Encryption Using LSB Steganography and RSA, International Journal of Engineering Research, 2019.

Alsaiari, S. A. A., LSB Steganography Using Pixel Locator Sequence with AES, Journal of Information Security, 2020.

Devi, S. R., & Rao, K. R., Double Layer Security Using Crypto–Stego Techniques, International Journal of Advanced Research in Computer Science, 2021.

D. Boneh and V. Shoup, A Graduate Course in Applied Cryptography, Stanford University, 2020.

## Document Link:

https://drive.google.com/drive/folders/1cXEqdfKEp4_8SrrXCYvPS84IVhKBTCL9
