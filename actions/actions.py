# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionConfirmarAgendamento(Action):
    def name(self) -> Text:
        return "action_confirmar_agendamento"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            servico = tracker.get_slot("servico_agendamento")
            data_hora = tracker.get_slot("data_hora_agenda")
            periodo = tracker.get_slot("periodo_agendamento_agenda")

            if servico and data_hora and periodo:
                mensagem = f"Seu agendamento foi confirmado!\nServiço: {servico}\nData: {data_hora}\nPeríodo: {periodo}"
            else:
                mensagem = "Parece que algumas informações estão faltando no agendamento."

            dispatcher.utter_message(text=mensagem)
        except Exception as e:
            dispatcher.utter_message(text=f"Erro ao executar a ação personalizada: {str(e)}")
            raise e

        return []
