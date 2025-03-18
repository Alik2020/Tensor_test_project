from pages.main import MainPage
import logging

logging.basicConfig(level=logging.INFO, filename="test2.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")


#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), '..')))

def test_2(browser):
    test_id = 'test_2'
    main_page = MainPage(browser)
    main_page.open()
    logging.info(f"{test_id} Открыта начальная страница")

    main_page.contacts()
    logging.info(f"{test_id} Успешный клик на контакты.")
    contacts_page = main_page.offices()
    logging.info(f"{test_id} Успешный клик на офисы.")
    
    region_init = 'Тамбовская обл.'
    region_actual = contacts_page.check_region()
    assert region_actual == region_init, logging.error(f"{test_id} не тот регион ({region_actual} вместо {region_init}!")
    logging.info(f"{test_id} Регион - {region_init} соответствует заявленному.")
    assert contacts_page.check_partners(), 'нет партнёров'

    partners = contacts_page.get_partners_text()
    region = "Камчатский край"

    assert contacts_page.change_region_check("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span", region), logging.error(f"{test_id} Регион не {region}!")
    logging.info(f"{test_id} Регион изменён.") 

    partners_new_region = contacts_page.get_partners_text()
    assert partners != partners_new_region, logging.error(f"{test_id} список партнёров остался тот же самый!")
    logging.info(f"{test_id} Список партнёров изменён.") 

    assert contacts_page.check_reg_in_url("kamchatskij-kraj"), logging.error(f"{test_id} url не содержит нужного текста!")
    logging.info(f"{test_id} url соответствует региону.")

    assert contacts_page.check_reg_in_title("Камчатский край"), logging.error(f"{test_id} Заголовок страницы не содержит нужного текста!")
    logging.info(f"{test_id} заголовок страницы соответствует региону.")

    