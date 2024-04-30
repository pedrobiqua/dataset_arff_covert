from scipy.io import arff
import pandas as pd
import os

class ArffDFClass:
    def __init__(self, datasets_path:str) -> None:
        """
        Recebe a pasta de datasets no formato arff e converte para o pandas.
        """
        self.datasets_path = datasets_path

    def _byte_to_string(self, d_bytes):
        """
        Converte uma lista de bytes para uma lista de strings.
        """
        return [value.decode('utf-8') if isinstance(value, bytes) else value for value in d_bytes]

    def _convert_colunm(self, df):
        """
        Converte a coluna que apresenta b'valor' em uma coluna de string
        """
        for column in df.columns:
            if(df[column].dtype == 'O'):
                df[column] = self._byte_to_string(df[column])
        return df
    
    def arff_to_df(self):
        """
        Transforma um datset escrito em arff para um dataframe do `pandas` e utiliza o `scipy` para fazer essa conversão
        """
        dataframes_list = []
        files = os.listdir(self.datasets_path)
        for file in files:
            # Carrega arquivo arff
            data, meta = arff.loadarff(f"{self.datasets_path}/{file}")
            df = pd.DataFrame(data)
            # Arruma o dataframe
            df = self._convert_colunm(df)
            # Monta csv
            name_dataframe = meta.name.replace("'", "")
            df.to_csv(f"{name_dataframe}.csv", index=False)
            dataframes_list.append(df)
            
            # Mostra como ficou montado o dataframe do pandas para o usuário
            print("Dataset Info:\n")
            print(df.info())
            
            # Se tiver a coluna class mostra na tela as classes
            if("class" in df.columns):
                print(f"\nClass:{df['class'].unique()}")
        
        return dataframes_list