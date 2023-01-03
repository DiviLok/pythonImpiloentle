# Impilointle Project

This is a project created by University West to help undeserved communities in South Africa with basic health information

## Requirements

> Internet is required during initial setup to install python dependencies. After installation, the application can run without an active internet connection

python 3.7+

## Technical information

Project is a simple python flask based application to display videos

## Installation steps

Running the setup.sh script will do all necessary steps to install the application, its dependencies and setup the application as a service.

Application will auto restart if the linux machine (raspberryPi) is restarted. No maintenance is required

### Linux
```bash
# Run the setup script to setup and install the project as a service
sh setup.sh

# To view status of service run below command
systemctl status impilointle

# To restart the service run below command
sudo systemctl restart impilointle

# To see logs run below command
journalctl -f
# These are flowing logs, press cntrl+C to exit logs
```

## Project Tree

```
pythonImpiloentle
├─ .vscode
│  └─ launch.json
├─ credentials.txt
├─ index.py
├─ requirements.txt
├─ static
│  ├─ audios
│  │  ├─ horse.ogv
│  │  ├─ Nutrition1.mp3
│  │  ├─ Nutrition3.mp3
│  │  ├─ Nutrition5.mp3
│  │  ├─ Nutrition6.mp3
│  │  ├─ Nutrition6Xhosa.mp3
│  │  └─ sputum.mp3
│  ├─ css
│  │  ├─ dashboard.css
│  │  ├─ font-awesome.min.css
│  │  ├─ login.css
│  │  ├─ main.css
│  │  └─ test.css
│  ├─ files
│  │  ├─ Intsholongwane_ka_gawulayo_ukhulelwe_HIV.mp4
│  │  └─ Isifo_sephepha_TB.mp4
│  ├─ fonts
│  │  └─ fontawesome-webfont.woff2
│  ├─ images
│  │  ├─ breastfeeding.png
│  │  ├─ circled-menu-icon.png
│  │  ├─ download.png
│  │  ├─ EarlyChildhoodProblems.jpg
│  │  ├─ EatingWellAndSavingMoney.png
│  │  ├─ external-listening-journalism-soft-fill-soft-fill-juicy-fish.png
│  │  ├─ favicon.ico
│  │  ├─ HIV.jpg
│  │  ├─ icons-download.png
│  │  ├─ immunization.jpg
│  │  ├─ nutrition and food.jpg
│  │  ├─ nutrition1.png
│  │  ├─ nutrition3.png
│  │  ├─ nutrition5.png
│  │  ├─ nutrition6.png
│  │  ├─ pregnancy.jpg
│  │  ├─ search.png
│  │  ├─ sputum.png
│  │  ├─ TB.jpeg
│  │  ├─ white-circled-menu-icon.png
│  │  └─ xhosaCulture.jpg
│  ├─ js
│  │  ├─ autoplay.js
│  │  ├─ dashboard.js
│  │  ├─ feature.js
│  │  └─ languagechange.js
│  └─ videos
│     ├─ earlychildhoodproblems
│     │  └─ Impawu ezinobungozi kubantwana abancinci (Dangers in Early Childhood).mp4
│     ├─ Early_Childhood
│     │  ├─ Impawu ezinobungozi kubantwana abancinci (Dangers in Early Childhood).mp4
│     │  ├─ Impilo yengqondo kumama onosana (Mental Health for new Mothers).mp4
│     │  └─ Ukuthintela abantwana (Immunization).mp4
│     ├─ eatwellandsavemoney
│     │  └─ Ukutya kakuhle wonge nemali (Eating Well and Saving Money).mp4
│     ├─ hiv
│     │  ├─ Intsholongwane ka gawulayo (HIV in Pregnancy).mp4
│     │  └─ test_Intsholongwane ka gawulayo ukhulelwe (HIV).mp4
│     ├─ Imifuno neziqhamo (Nutrition Fruits and Vegetables).mp4
│     ├─ immunization
│     │  └─ Ukuthintela abantwana (Immunization).mp4
│     ├─ Impawu ezinobungozi kubantwana abancinci (Dangers in Early Childhood).mp4
│     ├─ Impilo yengqondo kumama onosana (Mental Health for new Mothers).mp4
│     ├─ Intlobo zokutya (Macronutrients).mp4
│     ├─ Intsholongwane ka gawulayo (HIV in Pregnancy).mp4
│     ├─ Isifo sephepha (TB).mp4
│     ├─ Isifo_sephepha_(TB)
│     │  ├─ Isifo sephepha (TB).mp4
│     │  └─ Isikhohlela (Sputum).mp4
│     ├─ Isikhohlela (Sputum).mp4
│     ├─ Istatshi kukutya okunika amandla (Nutrition starch).mp4
│     ├─ Izakhamzimba ezibaluleke kakhulu (Nutrition vitamins).mp4
│     ├─ newmothers
│     │  ├─ Impilo yengqondo kumama onosana (Mental Health for new Mothers).mp4
│     │  ├─ Ubunzima bokuncancisa (Challenges with breastfeeding).mp4
│     │  └─ Ukuncancisa (Breastfeeding).mp4
│     ├─ Nutrition
│     │  ├─ Imifuno neziqhamo (Nutrition Fruits and Vegetables).mp4
│     │  ├─ Intlobo zokutya (Macronutrients).mp4
│     │  ├─ Istatshi kukutya okunika amandla (Nutrition starch).mp4
│     │  ├─ Izakhamzimba ezibaluleke kakhulu (Nutrition vitamins).mp4
│     │  ├─ Rec_0003.mp4
│     │  └─ Ukutya Xa Umama Ukhulelwe (Nutrition in Pregnancy).mp4
│     ├─ pregnancy
│     │  ├─ Intsholongwane ka gawulayo (HIV in Pregnancy).mp4
│     │  ├─ Rec_0003.mp4
│     │  └─ Ukutya Xa Umama Ukhulelwe (Nutrition in Pregnancy).mp4
│     ├─ tb
│     │  ├─ Isifo sephepha (TB).mp4
│     │  └─ Isikhohlela (Sputum).mp4
│     ├─ test_Intsholongwane ka gawulayo ukhulelwe (HIV).mp4
│     ├─ Ubunzima bokuncancisa (Challenges with breastfeeding).mp4
│     ├─ Ukuncancisa (Breastfeeding).mp4
│     ├─ Ukuthintela abantwana (Immunization).mp4
│     ├─ Ukutya kakuhle wonge nemali (Eating Well and Saving Money).mp4
│     └─ Ukutya Xa Umama Ukhulelwe (Nutrition in Pregnancy).mp4
├─ templates
│  ├─ about.html
│  ├─ categories.html
│  ├─ dashboard.html
│  ├─ home.html
│  ├─ login.html
│  ├─ navbar.html
│  ├─ pictures.html
│  ├─ upload.html
│  └─ videos.html
└─ __pycache__
   ├─ index.cpython-310.pyc
   └─ index.cpython-312.pyc

```