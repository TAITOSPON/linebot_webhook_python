import json
import dialogflow_v2 as dialogflow

class PostToDialog:


    def __new__(salf,project_id, session_id, texts, language_code):
    
        # session_client = dialogflow.SessionsClient()

        # session = session_client.session_path(project_id, session_id)

            
        # for text in texts:
        #     text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

        #     query_input = dialogflow.types.QueryInput(text=text_input)

        #     response = session_client.detect_intent(session=session, query_input=query_input)

        

        #     print('=' * 20)
        #     print('Query text: {}'.format(response.query_result.query_text))
        #     print('Detected intent: {} (confidence: {})\n'.format(
        #         response.query_result.intent.display_name,
        #         response.query_result.intent_detection_confidence))
        #     print('Fulfillment text: {}\n'.format(
        #         response.query_result.fulfillment_text))



        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(project_id, session_id)

        

        text_input = dialogflow.types.TextInput(text=texts, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(response.query_result.intent.display_name,response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))

        if str(response.query_result.intent.display_name) == "Default Fallback Intent" or str(response.query_result.intent.display_name) == "Default Welcome Intent":
            return str(response.query_result.fulfillment_text)
        else :
            return str(response.query_result.intent.display_name)

# texts = "สวัสดีครับ"
# a = PostToDialog("nuengdevtoat-ihq9","nuengdevtoat-ihq9",texts,'th')
# print('nueng = ',a)