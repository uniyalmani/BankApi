from fastapi import FastAPI
import pandas as pd
import os



app = FastAPI()



@app.on_event("startup")
def on_startup():
    try:
        global df
        print("starting ", "loding data")
        data_url = "app/data/bank_branches.csv"
        # data_url = "https://github.com/snarayanank2/indian_banks/blob/master/bank_branches.csv"
        df = pd.read_csv(data_url)
        # print(df.head)
    except Exception as e:
        print(e, "error message")
    print()


@app.get("/banks")
def get_banks():
    if df is None:
        return {"message": "NO data found"}
    banks = df['bank_name'].unique()
    total_banks = len(banks)
    return {"Total Banks": total_banks,'Banks': list(banks)}


@app.get("/branches/{bank_name}")
def get_branches(bank_name: str):
    if df is None:
        return {"message": "NO data found"}
    branches = df[df['bank_name'] == bank_name]
    total_branches = len(branches)
    return {"Total Branches": total_branches ,'Branches': branches.to_dict(orient='records')}


