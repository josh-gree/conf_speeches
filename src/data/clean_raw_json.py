import ujson
import pickle

data = ujson.decode(open('../../data/external/conf_speeches/data.json').read())

date = [int(dat['date'].split()[-1][:4]) for dat in data]
speaker = [dat['speaker'].split('(')[0].strip() for dat in data]
party = [dat['speaker'].split('(')[1][:-1] for dat in data]
text = [dat['text'].strip() for dat in data]

zip_dat = zip(date, speaker, party, text)
zip_dat = filter(lambda x: x[1] != 'Winston Churchill', zip_dat)
zip_dat = sorted(zip_dat, key=lambda x: x[0])

lib_dem_names = ['Liberal', 'Liberal Democrat', 'SDP-Liberal Alliance']
zip_dat_con = filter(lambda x: x[2] == 'Conservative', zip_dat)
zip_dat_lab = filter(lambda x: x[2] == 'Labour', zip_dat)
zip_dat_libdem = filter(lambda x: x[2] in lib_dem_names, zip_dat)


data_dict = {'date': map(lambda x: x[0], zip_dat),
            'speaker': map(lambda x: x[1], zip_dat),
            'party': map(lambda x: x[2], zip_dat),
            'text': map(lambda x: x[3], zip_dat)}

con_data_dict = {'date': map(lambda x: x[0], zip_dat_con),
            'speaker': map(lambda x: x[1], zip_dat_con),
            'party': map(lambda x: x[2], zip_dat_con),
            'text': map(lambda x: x[3], zip_dat_con)}

lab_data_dict = {'date': map(lambda x: x[0], zip_dat_lab),
            'speaker': map(lambda x: x[1], zip_dat_lab),
            'party': map(lambda x: x[2], zip_dat_lab),
            'text': map(lambda x: x[3], zip_dat_lab)}

libdem_data_dict = {'date': map(lambda x: x[0], zip_dat_libdem),
            'speaker': map(lambda x: x[1], zip_dat_libdem),
            'party': map(lambda x: x[2], zip_dat_libdem),
            'text': map(lambda x: x[3], zip_dat_libdem)}


pickle.dump(data_dict, open(
    "../../data/processed/processed_data.p", "wb"))

pickle.dump(con_data_dict, open(
    "../../data/processed/processed_data_con.p", "wb"))

pickle.dump(lab_data_dict, open(
    "../../data/processed/processed_data_lab.p", "wb"))

pickle.dump(libdem_data_dict, open(
    "../../data/processed/processed_data_libdem.p", "wb"))
