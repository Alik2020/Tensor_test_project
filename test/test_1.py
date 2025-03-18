from pages.main import MainPage
import logging

def test_1(browser):
    test_id = 'test_1'
    main_page = MainPage(browser)
    main_page.open()
    logging.info(f"{test_id} Открыта начальная страница")

    main_page.contacts()
    logging.info(f"{test_id} Успешный клик на контакты.")
    contacts_page = main_page.offices()
    logging.info(f"{test_id} Успешный клик на офисы.")

    tensor_page = contacts_page.tensor()

    assert tensor_page.force_in_people_search(), logging.error(f"{test_id} Раздела 'Сила в людях' нет или он продублирован")
    logging.info(f"{test_id} Проверка 'Сила в людях' пройдена")

    about_page = tensor_page.force_about()
    intended_url = "https://tensor.ru/about"
    assert about_page.check_url(intended_url), logging.error(f"{test_id} Не удалось перейти по ссылке {intended_url}")
    logging.info(f"{test_id} Текущий url: {intended_url}")

    sizes = about_page.get_image_sizes()
    assert all(size == sizes[0] for size in sizes), logging.error(f"{test_id} Размеры картинок разные")
    logging.info(f"{test_id} Размеры картинок одинаковые")
