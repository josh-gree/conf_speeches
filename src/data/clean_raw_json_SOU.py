import ujson
import pickle

data = ujson.load(open('../../data/external/SOU/data.json'))

date = [dat['date'] for dat in data]
speaker = [dat['speaker'] for dat in data]
text = [dat['text'] for dat in data]

zip_dat = zip(date,speaker,text)
zip_dat = sorted(zip_dat,key=lambda x : x[0])

data_dict = {'date':map(lambda x: x[0], zip_dat),
'speaker':map(lambda x: x[1], zip_dat),
'text':map(lambda x: x[2], zip_dat)
}

pickle.dump(data_dict, open(
    "../../data/processed/sou_processed_data.p", "wb"))
