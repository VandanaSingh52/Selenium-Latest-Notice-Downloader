# Selenium-Latest-Notice-Downloader

A Python script that uses Selenium to download the latest PDF file from the Supreme Court of India website.

# Description

This project is a simple and automated way to get the latest notice or circular from the Supreme Court of India website (https://main.sci.gov.in/notices-circulars).
It uses Selenium to open the website, locate and click on the link to the latest PDF file, and download it to a specified directory.
It can be useful for anyone who needs to keep track of the latest updates from the Supreme Court of India.

# Usage

1. Clone the repository to your local machine:

`git clone <repository_url>`

2. Change Project directory

`cd Selenium-Latest-Notice-Downloader`

2. Install the required dependencies:

`pip install -r requirements.txt`

3. To run the script, execute the following command in the terminal:

`pytest \path\to\test_latestnotice.py`

The script will open the Chrome browser, navigate to the Supreme Court of India website, click on the link to the latest PDF file, and download it to the Downloads directory. The script will close the browser and exit after the download is complete.

# Configuration

You can change the download directory by modifying the get_download_directory method in the script. You can also change the wait time for the link element by modifying the WebDriverWait parameter in the script.

# License

This project is licensed under the MIT License.
