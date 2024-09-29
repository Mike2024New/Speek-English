# важно устанавливать конкретную версию: pip install googletrans==4.0.0-rc1
from googletrans import Translator


class TranslateFrases:
    _TRANSLATOR = Translator()

    def __init__(self, lang_input: str, lang_output: str) -> None:
        """
        :param lang_input: язык фразы подлежащей переводу
        :param lang_output: язык на который нужно перевести
        """
        self._lang_input = lang_input
        self._lang_output = lang_output

    def _translate_phrase(self, phrase_eng: str) -> dict:
        """
        Получение перевода фразы с Английского языка на Русский
        :param phrase_eng: фраза на Английском языке
        :return: словарь из пары ru (перевод фразы) eng (исходный текст из phrase_eng)
        Пример:
        input: "They'd like to call us."
        output: {'ru': 'Они хотели бы позвонить нам.', 'en': "They'd like to call us."}
        """
        try:
            # получить перевод
            result = self._TRANSLATOR.translate(phrase_eng, src=self._lang_input, dest=self._lang_output)
            return {self._lang_output: result.text, self._lang_input: phrase_eng}
        except TypeError:
            raise TypeError(f"Ошибка: переданный объект ({phrase_eng}) должен быть строкой.")
        except Exception as err:
            raise Exception(f"Непредвиденная ошибка: переданный объект {phrase_eng}, текст ошибки: {err}")

    def get_translate_dict(self, data: str) -> list:
        """
        перевод 1 или нескольких фраз, на вход принимает строку, строка разделенная переносами строки "\n"
        воспринимается как несколько фраз и обрабатывается split для нарезки фраз
        :param data: входная строка с фразами
        :return: список словарей.
        Пример:
        input: "I'd like to hear this story."
        output:
        [{'ru': 'Я хотел бы услышать эту историю.', 'en': "I'd like to hear this story."},]
        """
        if not isinstance(data, str):
            raise TypeError("На вход принимается только строка")
        if len(data) == 0:
            raise ValueError("Строка не должна быть пустой")
        print("подождите идёт перевод...")
        list_of_phrases = set(phrase.lstrip().rstrip() for phrase in data.split("\n") if len(phrase) > 4)
        return list(map(self._translate_phrase, list_of_phrases))  # получаем перевод фраз


if __name__ == '__main__':
    input_data = """
    I'd like to hear this story.
    I'd like to read this book.
    I'd like to buy a house.
    """
    translate_phrases = TranslateFrases(lang_input='en', lang_output='ru')
    res = translate_phrases.get_translate_dict(data="""She'd like to talk with me.""")
    # res = translate_phrases.get_translate_dict(data=input_data)
    [print(phrase) for phrase in res]
