import pandas as pd
import numpy as np
import re

PATH = './data/output_dir/'

def delete_short_data(csv_path):
    data = pd.read_csv(csv_path)
    print(data.head())

    data = data.dropna()
    data = data.drop_duplicates()


    data["text"] = data["text"].str.replace(r" ", " ", regex=True) # remove extra space
    data["text"] = data["text"].str.replace(r"-\{[A-Za-z]\|[^{}]+\}-", "", regex=True) # remove -{H|英文:中文;英文:中文;}-
    data["text"] = data["text"].str.replace("-{T|zh:-{zh|}-;zh-hans:-{zh-hans|}-;zh-hant:-{zh-hant|}-;zh-cn:-{zh-cn|}-;zh-hk:-{zh-hk|}-;zh-mo:-{zh-mo|}-;zh-my:-{zh-my|}-;zh-sg:-{zh-sg|}-;zh-tw:-{zh-tw|}-;}-", "") # remove -{T|zh:-{zh|}-;zh-hans:-{zh-hans|}-;zh-hant:-{zh-hant|}-;zh-cn:-{zh-cn|}-;zh-hk:-{zh-hk|}-;zh-mo:-{zh-mo|}-;zh-my:-{zh-my|}-;zh-sg:-{zh-sg|}-;zh-tw:-{zh-tw|}-;}-
    data["text"] = data["text"].str.replace("-\{\}-", "")
    data["text"] = data["text"].str.replace(r"[\「\(\[\{\（\【\《][^\w\u4e00-\u9fa5]*[\)\]\}\）\】\」\》]", "", regex=True) # remove （）[]【】「」《》

    data = data.drop(data[data['text'].map(len) < 200].index)
    print(data.shape)
    data.to_csv(PATH + "deleted_data_5000.csv", index=False)

if __name__ == "__main__":
    delete_short_data(PATH + "cleaned_5000.csv")