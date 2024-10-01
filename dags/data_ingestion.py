import pandas as pd
import numpy
from Data_Connector_Modules.Google_Ads import Google_Ads
from Data_Connector_Modules.Google_Sheet import Google_Sheet
from Data_Connector_Modules.Facebook_Ads import Facebook_Ads
from Data_Connector_Modules.Taboola import Taboola

data_sources_list = ["Google_Ads", "Google_Sheet", "Facebook_Ads", "Taboola"]

def append_to_postgress(pandas_dataframe):
    pass

def factory(source_name : str , **kwargs):
    pandas_dataframe = None

    if source_name == "Google_Ads":
        google_ads_instance = Google_Ads()
        fetched_response = google_ads_instance.fetch()
        cleaned_response = google_ads_instance.clean(fetched_response = fetched_response)
        pandas_dataframe = google_ads_instance.return_as_dataframe(cleaned_response = cleaned_response)

    elif source_name == "Google_Sheet":
        google_sheet_instance = Google_Sheet()
        fetched_response = google_sheet_instance.fetch()
        cleaned_response = google_sheet_instance.clean(fetched_response = fetched_response)
        pandas_dataframe = google_sheet_instance.return_as_dataframe(cleaned_response = cleaned_response)

    elif source_name == "Facebook_Ads":
        facebook_ads_instance = Facebook_Ads()
        fetched_response = facebook_ads_instance.fetch()
        cleaned_response = facebook_ads_instance.clean(fetched_response = fetched_response)
        pandas_dataframe = facebook_ads_instance.return_as_dataframe(cleaned_response = cleaned_response)

    elif source_name == "Taboola":
        taboola_instance = Taboola()
        fetched_response = taboola_instance.fetch()
        cleaned_response = taboola_instance.clean(fetched_response = fetched_response)
        pandas_dataframe = taboola_instance.return_as_dataframe(cleaned_response = cleaned_response)

    append_to_postgress(pandas_dataframe)

    return None

if __name__ == "__main__":
    for source in data_sources_list:
        factory(source)
