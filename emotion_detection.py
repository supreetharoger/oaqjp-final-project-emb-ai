import json
import requests

def emotion_detector(text_to_analyze: str) -> str:
    response = requests.post(
        url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyze } },
    )
    response_dict = {}
    if response.status_code == 200:
        response_dict = json.loads(response.text)
    return response_dict

result = emotion_detector("I love this new technology")
print(result)