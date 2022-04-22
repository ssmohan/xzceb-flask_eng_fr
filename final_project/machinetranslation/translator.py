"""Language translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """englisg to french translation"""
    #write the code here
    frn_txt = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return frn_txt.get("translations")[0].get("translation")

def french_to_english(french_text):
    """french to english"""
    eng_txt = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return eng_txt.get("translations")[0].get("translation")
