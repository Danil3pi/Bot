import random
import nltk

# какая-то структура данных
BOT_CONFIG = {
    'intents' : {

        'hello' : {
            'examples' : ["Привет", "Добрый день", "Привки"],
            'responses' : ["Привет человек!", "И вам здравствуйте", "Мои создатели создали меня спецом для тебя"]
        },
        'bye' : {
            'examples' : ["Пока", "До скорой встречи"],
            'responses' : ["Увидимся!", "Покеда"]
        },
        'name' : {
            'examples' : ["Как тебя зовут?", "Представься", "Скажи свое имя"],
            'responses' : ["Меня зовут Саша"]
        }
    },

    'failer_phrases' : ['Непонятно, перепиши по человечаииии',
                    'Я еще только учусь, спроси что-то другое',
                    'Ты точно написал правильно?',
                    "Слишком сложный вопрос для меня"]
}


def clear_phrase(phrase):
    phrase = phrase.lower()
    alphabet = 'абвгдеёжзийклмнопрстуфхцщшъыьэюя- '

    #result = ''.join()

    result = ''
    for symbol in phrase:
        if symbol in alphabet:
            result += symbol

    return result


def classify_intent(user_replica):
    # TODO
    user_replica = clear_phrase(user_replica)
    for intent_key, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            distance = nltk.edit_distance(example, user_replica)
            distance /= len(user_replica)
            if distance < 0.4:
                return intent_key

def generate_answer(replica):
    # TODO na 3 day
    return None


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        responses = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)


def get_failer_phrase():
    failer_phrases = BOT_CONFIG['failer_phrases']
    return random.choice(failer_phrases)


def bot(replica):
    """
    :param replica:
    :return:
    """
    # NLU
    intent = classify_intent(replica)
    # Генерация ответа
    # Заготовленные реплики
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer


    # вызов генеративной модели
    answer = generate_answer(replica)
    if answer:
        return answer

    # заглушка
    return get_failer_phrase()

print(classify_intent('Добрый вечер'))