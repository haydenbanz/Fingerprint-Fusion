# Fingerprint Fusion 🤖👍
![DiscordGloom Logo](https://github.com/haydenbanz/Fingerprint-Fusion/blob/main/banner.png?raw=true)
[![Python - Fingerprint Fusion](https://img.shields.io/static/v1?label=Python&message=Fingerprint%20Fusion&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge&&logo=python)](https://github.com/haydenbanz/Fingerprint-Fusion/)
[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=%233DA639&labelColor=%23e3e3e3&style=for-the-badge)](https://github.com/haydenbanz/Fingerprint-Fusion/blob/main/LICENSE)
[![Python Version](https://img.shields.io/static/v1?label=Python&message=3.6%2B&color=%230078D6&labelColor=%23e3e3e3&style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![Flask Framework](https://img.shields.io/static/v1?label=Flask&message=Web%20Framework&color=%23FFFFFF&labelColor=%23000000&style=for-the-badge)](https://pypi.org/project/Flask/)
[![GitHub Issues](https://img.shields.io/github/issues/haydenbanz/Fingerprint-Fusion?style=for-the-badge)](https://github.com/haydenbanz/Fingerprint-Fusion/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haydenbanz/Fingerprint-Fusion?style=for-the-badge)](https://github.com/haydenbanz/Fingerprint-Fusion/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/haydenbanz/Fingerprint-Fusion?style=for-the-badge)](https://github.com/haydenbanz/Fingerprint-Fusion/stargazers)
![Profile Views](https://komarev.com/ghpvc/?username=haydenbanz&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)


## 📖 Description

🔍👆 Fingerprint Fusion 👆🔍

This Python application is your ultimate tool for fingerprint analysis and matching against a comprehensive database. Harnessing advanced image processing techniques and machine learning, Fingerprint Fusion brings cutting-edge technology to identify and match fingerprints with precision. 🌐✨

Explore the world of biometric security with this powerful Flask-based web application. 🚀

    🔍 Fingerprint Analysis: Leverage sophisticated image processing to extract and analyze fingerprint patterns.
    🔄 Database Matching: Utilize machine learning algorithms to match fingerprints against a secure and expansive database.
    🖼️ Image Enhancement: Optimize fingerprint images for accurate and efficient identification.
    🌐 Flask Framework: Powered by Flask, Fingerprint Fusion provides a seamless and user-friendly web interface.
    📊 Data Insights: Gain valuable insights and statistical data on fingerprint matches.

Empower your security solutions with Fingerprint Fusion! 👤🔒

Feel free to adjust the emojis and descriptions according to your preferences!
## Features
- Fingerprint image preprocessing.
- Feature extraction from fingerprint images.
- Training a machine learning model for fingerprint matching.
- Matching fingerprint images with a database.
- Evaluation of matching performance.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- scikit-learn (if using machine learning)
- [Database of Fingerprint Images] (provide details or a link if available)
  
## File structure
FingerprintFusion/<br>
|-- FingerprintFusion.py<br>
|-- app.py<br>
|-- icon.ico<br>
|-- README.md<br>
|-- templates/<br>
|   |-- index.html<br>
|   |-- results.html<br>
|-- fingerprint/<br>
|-- icon.png<br>


- **FingerprintFusion.py:** Main script forwindows OS.
- **app.py:** Flask application script(Mainly for linux & MAC. Also supported for windows).
- **icon.ico and icon.png:** Icon files for the project.
- **README.md:** Documentation for the project.
- **templates/:** Directory containing HTML templates for the Flask application.
  - **index.html:** Template for the main page.
  - **results.html:** Template for displaying fingerprint matching results.
- **fingerprint/:** Directory where fingerprint images are stored(jpg formant).

## Getting Started(Windows Installation)
To get started with Fingerprint-Fusion , follow these steps:

1. Clone this repository:`git clone https://github.com/haydenbanz/Fingerprint-Fusion`
  
  
 2.`cd Fingerprint-Fusion`

3. Place your target fingerprint image (e.g., `img0026.jpg`) in the main.py file.

4. Organize your template fingerprint images in a folder (e.g., `fingerprint/`) within the project directory.

5. Run the code:
 `python FingerprintFusion.py`


6. The code will iterate through the template fingerprint images in the specified folder, compare each template with the target image, and print the match score for each template.

## Customization

You can customize the code further by modifying the following functions in the `main.py` file:

* `preprocess_fingerprint()`: This function applies preprocessing steps to the fingerprint images. You can modify this function to add your own preprocessing steps.
* `match_fingerprint()`: This function compares two fingerprint images and returns the match score. You can modify this function to use a different matching algorithm.

  For Linux installation, you would typically use the following steps. Please note that these are general instructions and may need adjustment based on your specific system and setup.

## Flask Installation on Linux

1. **Install Python:**
   Ensure you have Python installed. You can check by running:
   ```bash
   python3 --version
   ```
   If Python is not installed, you can install it using your package manager. For example, on Debian-based systems:
   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

2. **Install Flask:**
   Install Flask using `pip`, the Python package installer:
   ```bash
   sudo apt-get install python3-pip
   pip3 install flask
   ```

3. **Clone the Repository:**
   Clone your Flask project repository:
   ```bash
   git clone https://github.com/haydenbanz/Fingerprint-Fusion
   cd Fingerprint-Fusion
   ```

4. **Install Dependencies:**
   Install the required Python packages for your project:
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the Flask App:**
   Run your Flask application:
   ```bash
   python3 app.py
   ```

   This will start the development server. Open your web browser and go to `http://127.0.0.1:5000/` to see your Flask app.


Happy fingerprint matching!





### Contributing

Contributions to Fingerprint Glitch are welcome! To contribute to this project, follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them.
5. Push your changes to your fork.
6. Create a pull request on GitHub.
## Contact

If you have any questions or feedback, please contact the project maintainers:

* 0x_hayden
* Email: t5hlt8zcp@mozmail.com
## Credits

This project is maintained by:

[<img src="https://avatars.githubusercontent.com/u/135024483?s=48&v=4" width="64" height="64" alt="Contributor Name">](https://github.com/code-glitchers)

### Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="Contributor Name">](https://github.com/mindglitchers)
[<img src="https://avatars.githubusercontent.com/u/116929670?s=64&v=4" width="64" height="64" alt="Contributor Name">](https://github.com/AldrinCode)


## Support

If you find this project helpful, consider buying us a coffee:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/ciph3r#pageMessageModal)


## License

Fingerprint Glitch is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
## Contact


   
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.x-brightgreen.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange.svg)](https://opencv.org/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)





