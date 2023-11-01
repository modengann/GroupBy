import pandas as pd

def main():
    
    wh = pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")
    wh3 = wh.rename(columns={"m": "Month", "d": "Day", "Precipitation amount (mm)" : "Precipitation", "Snow depth (cm)" : "Snow", "Air temperature (degC)" : "Temperature"})
    print(wh3)






if __name__ == "__main__":
    main()