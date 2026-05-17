import random


def primarchs_data ():
    data = [
        {
            'name': 'Альфарий',
            'quote': '«Я — Альфарий.»',
            'image': 'images/primarh/Alpharius.webp'
        },
        {
            'name': 'Ангрон',
            'quote': '«Смерть не имеет значения! Значение имеет лишь пролитая кровь!»',
            'image': 'images/primarh/Angron.webp'
        },
        {
            'name': 'Корвус Коракс',
            'quote': '«Мы приходим из теней, и в тени мы возвращаемся. Никогда больше.»',
            'image': 'images/primarh/Corax.webp'
        },
        {
            'name': 'Феррус Манус',
            'quote': '«Плоть слаба. Только металл способен выдержать испытание временем.»',
            'image': 'images/primarh/FerrusManus.webp'
        },
        {
            'name': 'Фулгрим',
            'quote': '«Мы должны стремиться к совершенству во всём, иначе зачем вообще существовать?»',
            'image': 'images/primarh/Fulgrim.webp'
        },
        {
            'name': 'Робут Гиллиман',
            'quote': '«Мы — строители нового будущего. Мы — защитники человечества.»',
            'image': 'images/primarh/Guilliman.webp'
        },
        {
            'name': 'Хорус Луперкаль',
            'quote': '«Пусть Галактика горит!»',
            'image': 'images/primarh/Horus.webp'
        },
        {
            'name': 'Джагатай Хан',
            'quote': '«Смейся, убивая. Ибо нет ничего более прекрасного, чем скорость и свобода.»',
            'image': 'images/primarh/Jaghatai_Khan.webp'
        },
        {
            'name': 'Конрад Кёрз',
            'quote': '«Смерть — ничто по сравнению с правосудием.»',
            'image': 'images/primarh/KonradCurze.webp'
        },
        {
            'name': 'Леман Русс',
            'quote': '«Там, где другие видят дикость, я вижу чистоту. Мы — палачи Императора.»',
            'image': 'images/primarh/LemanRuss.webp'
        },
        {
            'name': 'Лев Эль\'Джонсон',
            'quote': '«Верность — это своя собственная награда.»',
            'image': 'images/primarh/LionElJonson.webp'
        },
        {
            'name': 'Лоргар Аврелиан',
            'quote': '«Всякая истина начинается с веры.»',
            'image': 'images/primarh/Lorgar.webp'
        },
        {
            'name': 'Магнус Красный',
            'quote': '«Знание — это сила. Игнорировать его — значит быть рабом невежества.»',
            'image': 'images/primarh/Magnus.webp'
        },
        {
            'name': 'Мортарион',
            'quote': '«Стойкость и разрушение. Неотвратимость смерти — наш главный дар.»',
            'image': 'images/primarh/Mortarion.webp'
        },
        {
            'name': 'Пертурабо',
            'quote': '«Нет крепости, которую мы не могли бы сломить. Нет стены, что выстоит перед нами.»',
            'image': 'images/primarh/Perturabo.webp'
        },
        {
            'name': 'Рогал Дорн',
            'quote': '«Я — преторианец Императора. Ни одна твердыня не падет, если я её защищаю.»',
            'image': 'images/primarh/RogalDorn.webp'
        },
        {
            'name': 'Сангвиний',
            'quote': '«Лишь ангелы могут летать, но лишь люди могут падать. Мы же несем в себе и то, и другое.»',
            'image': 'images/primarh/Sanguinius.webp'
        },
        {
            'name': 'Вулкан',
            'quote': '«В пламени кузни отсекается слабость. Вулкан жив!»',
            'image': 'images/primarh/Vulkan.webp'
        }
    ]
    primarch = random.choice(data)
    return primarch