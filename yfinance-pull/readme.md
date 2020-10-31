## ***Files***
- **pull_data.py** Script.
- **pull_draft.ipynb** Explains how it works and partly demonstrates it.
- **read_sample.ipynb** Shows basic use case/ how to read the data.

#### **pull_data.py**
Utilizes [yfinance](https://github.com/ranaroussi/yfinance) to pull out the most current data —seperated by "sectors"— and write them into dataframes. Then, export them into csv files for easier access and manipulation.

![result](https://i.imgur.com/IFiZcIs.png)

Just make sure you have a csv (like provided) which seperate these stocks into sectors.

![sample](https://i.imgur.com/SkEs6fi.png)

This code (from the sample-read file) basically reads every file and puts it into Dataframes, so you don't have to run the script every day, yay!

![code](https://i.imgur.com/a6kNa9F.png)
