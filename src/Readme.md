# Setting up the development environment
To setup the development environment, follow the following steps:

1. **Clone the repository**:
`git clone git@github.com:osipra/Weather-Report.git`
2. Install `pyhton`
    sudo apt install python3
3. Instal `pip`
sudo apt install python3-pip
4. Install `virtualenv`
`sudo apt install python3.10-venv`
5. Create a virtual environment for the project
`python3 -m venv weather-project`
6. Activate the `virtualenv`
`source weather-project/bin/activate`
7. Install required dependencies
`pip install -r requirements.txt`
8. Run the project
`python3 main.py`