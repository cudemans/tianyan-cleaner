import pandas as pd

class CleanTianyanData:
    

    """ 
    Class to process data funding from Tianyancha.

    Required imports: Pandas, Numpy

    Arguments: Data file in JSON or csv format

    Returns: A cleaned dataframe with only international
        investments

    """

    def __init__(self, df): 
        
        if '.json' in str(df):
            self.df = pd.read_json(df)
        else:
            self.df = pd.read_csv(df)

    def clean_data(self):

        """
        This method replaces Chinese funding information
        with information translated into English.

        clean_data is called in the process_internationals
        and get_info methods

        """

        entry = self.df['funding round']
        entry.replace('战略融资', 'Venture Round',inplace=True)
        entry.replace('A轮', 'Series A',inplace=True)
        entry.replace('B轮', 'Series B',inplace=True)
        entry.replace('C轮', 'Series C',inplace=True)
        entry.replace('D轮', 'Series D',inplace=True)
        entry.replace('E轮', 'Series E',inplace=True)
        entry.replace('F轮', 'Series F',inplace=True)
        entry.replace('G轮', 'Series G',inplace=True)
        entry.replace('H轮', 'Series H',inplace=True)

        entry.replace('A+轮', 'Series A+',inplace=True)
        entry.replace('B+轮', 'Series B+',inplace=True)
        entry.replace('C+轮', 'Series C+',inplace=True)
        entry.replace('D+轮', 'Series D+',inplace=True)
        entry.replace('E+轮', 'Series E+',inplace=True)
        entry.replace('F+轮', 'Series F+',inplace=True)
        entry.replace('G+轮', 'Series G+',inplace=True)

        entry.replace('A++轮', 'Series A++',inplace=True)
        entry.replace('B++轮', 'Series B++',inplace=True)
        entry.replace('C++轮', 'Series C++',inplace=True)
        entry.replace('D++轮', 'Series D++',inplace=True)
        entry.replace('E++轮', 'Series E++',inplace=True)
        entry.replace('F++轮', 'Series F++',inplace=True)
        entry.replace('G++轮', 'Series G++',inplace=True)

        entry.replace('并购', 'Acquisition',inplace=True)
        entry.replace('天使轮', 'Angel Round',inplace=True)
        entry.replace('种子轮', 'Seed Round',inplace=True)
        entry.replace('股权转让', 'Equity Transfer',inplace=True)
        entry.replace('股权融资', 'Equity Financing',inplace=True)
        entry.replace('定向增发', 'Private Placement',inplace=True)
        entry.replace('债权融资', 'Debt Financing',inplace=True)

        # Translate amounts - This still needs work
        amounts = self.df.amount
        amounts.replace('未披露', 'Undisclosed', inplace=True)

        self.df = self.df
        return self.df

    def process_internationals(self):
        
        """ 
        Subsets dataset to only include international companies
        
        """
        
        self.clean_data()
        new_df = self.df.copy()
        new_df.full_name.fillna('international', inplace=True)
        new_df['international'] = new_df.full_name.map({'international': True})
        return new_df[new_df.international == True].drop('full_name', axis=1)
    
    
    def __str__(self):
        return f"{self.df.info()} \n \n Shape: \n {self.df.shape}"
