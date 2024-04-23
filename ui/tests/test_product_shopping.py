from ui.tests.base_selenium_test import BaseSeleniumTest


class TestProductShopping(BaseSeleniumTest):
    product_name: str

    def setUp(self) -> None:
        super().setUp()
        self.product_name = 'Sauce Labs Bike Light'

    def test_product_shopping(self):
        # 1. Login page
        self.pages.login_page.open()
        self.assert_page_url(page_url=self.pages.login_page.get_url())
        self.pages.login_page.login(username='standard_user', password='secret_sauce')

        # 2. Inventory page
        self.assert_inventory_page()

        # get product price which can change over time, so we ca calculate tax and total price dynamically
        product_price_str = self.pages.inventory_page.get_item_price(product_name=self.product_name)
        product_price = float(product_price_str.replace('$', ''))

        self.pages.inventory_page.add_to_cart(product_name=self.product_name)
        self.pages.inventory_page.go_to_cart()

        # 3. Cart page
        self.assert_cart_page(product_price=product_price_str)
        self.pages.cart_page.go_to_next_step()

        # 4. Checkout page
        self.assert_page_url(page_url=self.pages.checkout_page.get_url())
        self.assertEqual(self.pages.checkout_page.get_title(), 'Checkout: Your Information', msg='Page title wrong')
        self.pages.checkout_page.fill_payment_details(first_name='Test', last_name='Test', postal_code='123456')
        self.pages.checkout_page.go_to_next_step()

        # 5. Checkout Overview page
        self.assert_checkout_overview_page(product_price=product_price)
        self.pages.checkout_overview_page.finish_payment()

        # 6. Checkout Complete page
        self.assert_checkout_complete_page()
        self.pages.checkout_complete_page.back()

        # 7. Inventory page
        self.assert_page_url(page_url=self.pages.inventory_page.get_url())

    def assert_page_url(self, page_url: str):
        self.assertEqual(page_url, self.driver.current_url, msg='Page url wrong')

    def assert_inventory_page(self):
        self.assert_page_url(page_url=self.pages.inventory_page.get_url())

        number_of_products: int = self.pages.inventory_page.items_count()
        self.assertGreater(number_of_products, 0, msg='No products to select')

    def assert_cart_page(self, product_price: str):
        self.assert_page_url(page_url=self.pages.cart_page.get_url())

        number_of_items: int = self.pages.cart_page.items_count()
        self.assertEqual(number_of_items, 1, msg='More than one product selected')

        cart_product_price: str = self.pages.cart_page.get_item_price(product_name=self.product_name)
        self.assertEqual(product_price, cart_product_price, msg='Product price different in the cart from the one on inventory page')

        cart_qty: str = self.pages.cart_page.get_item_quantity(product_name=self.product_name)
        self.assertEqual(cart_qty, 1, msg='Selected product quantity not equals 1')

    def assert_checkout_overview_page(self, product_price: float):
        self.assert_page_url(page_url=self.pages.checkout_overview_page.get_url())
        self.assertEqual(self.pages.checkout_overview_page.get_title(), 'Checkout: Overview', msg='Page title wrong')

        payment_info: str = self.pages.checkout_overview_page.get_payment_info()
        self.assertEqual(payment_info, 'SauceCard #31337', msg='Payment info wrong')

        shipping_info: str = self.pages.checkout_overview_page.get_shipping_info()
        self.assertEqual(shipping_info, 'Free Pony Express Delivery!', msg='Shipping info wrong')

        price_subtotal: str = self.pages.checkout_overview_page.get_price_subtotal()
        self.assertEqual(price_subtotal, f'Item total: ${product_price}', msg='Price subtotal wrong')

        expected_tax: float = product_price * 0.08
        price_tax: str = self.pages.checkout_overview_page.get_price_tax()
        self.assertEqual(price_tax, f'Tax: ${expected_tax:.2f}', msg='Price tax wrong')

        expected_total: float = product_price + expected_tax
        price_total: str = self.pages.checkout_overview_page.get_price_total()
        self.assertEqual(price_total, f'Total: ${expected_total:.2f}', msg='Price total wrong')

    def assert_checkout_complete_page(self):
        self.assert_page_url(page_url=self.pages.checkout_complete_page.get_url())
        self.assertEqual(self.pages.checkout_complete_page.get_title(), 'Checkout: Complete!', msg='Page title wrong')

        checkout_header_text: str = self.pages.checkout_complete_page.get_complete_header_text()
        self.assertEqual(checkout_header_text, 'Thank you for your order!', msg='Checkout header text wrong')

        checkout_msg: str = self.pages.checkout_complete_page.get_complete_label_text()
        self.assertEqual(checkout_msg, 'Your order has been dispatched, and will arrive just as fast as the pony can get there!',
                         msg='Checkout message text wrong')
