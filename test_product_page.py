from .PageObject.product_page import ProductPage
import pytest


@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6,
                                    pytest.param(7, marks=pytest.mark.xfail(reason="fixing this bug right now")), 8, 9])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_book_name()
    product_page.should_be_book_price()

    # pytest -rx -v test_product_page.py
