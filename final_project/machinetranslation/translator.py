import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))

def englishToFrench(englishText):
    #write the code here
    frenchTranslation - language_translator.translate(text=englishText, model_id='en-fr').get_result();
    return frenchToEnglish.get("translations")[0].get("trnaslation")

def frenchToEnglish(frenchText):
    #write the code here
    engishTranslation - language_translator.translate(text=frenchText, model_id='fr-en').get_result();
    return engishTranslation.get("translations")[0].get("trnaslation")