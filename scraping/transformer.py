import pandas as pd

def Transformer(data):

    #Dataframe kosong
    df = pd.DataFrame(columns = ['No.', 'Nama', 'Kekayaan bersih (USD)', 'Usia',
                                 'Kebangsaan', 'Sumber kekayaan', 'Tahun'])
    
    #Dictionary berisi key:value {tahun:index} dari variabel data
    IndexData = {2018:2}
    for i in IndexData:
        item = data[IndexData[i]]
        item['Tahun'] = i
        df = df.append(data[IndexData[i]])
    
    df = df.drop('No.', axis = 1)
    df.insert(0, 'Nomor Urut', range(1, 1 + len(df)))

    #Mengubah satuan miliar menjadi satuan juta
    df['Kekayaan bersih (USD)'] = df['Kekayaan bersih (USD)'].str.replace('miliar', '')
    df['Kekayaan bersih (USD)'] = df['Kekayaan bersih (USD)'].str.replace('$', '')
    df['Kekayaan bersih (USD)'] = '$' + (df['Kekayaan bersih (USD)'].astype(float)*1000).astype(str) + ' juta'

    return df
   