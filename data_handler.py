import pandas as pd 


class datahandler:
    def __init__(self):
        self.df = None
    
    def load_dataset(self,path):
        try:
            self.df = pd.read_csv(path)
            return True
        except Exception as e:
            print("Error Occured Cant Load Dataset")
            return False

    def get_dataframe(self):
        return self.df
    
    def get_columns(self):
        return list(self.df.columns)
    
    def get_numeric_columns(self):
        return list(self.df.select_dtypes(["int","float"]).columns)
    
    def get_categorical_columns(self):
        return list(self.df.select_dtypes(["category","O"]).columns)
    
    def get_preview(self,n_rows=5):
        return self.df.head(n_rows)
    
    def get_column_types(self):
        return dict(self.df.dtypes)
    
    def clear_data(self):
        self.df = None

