cart_items = []
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import os

print(os.path.exists("assets/images/dress.jpg"))
print(os.path.exists("assets/images/top.jpg"))
print(os.path.exists("assets/images/jeans.jpg"))

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='ZYKAZ LOGIN', font_size=30))

        self.username = TextInput(hint_text='Username')
        self.password = TextInput(hint_text='Password', password=True)

        layout.add_widget(self.username)
        layout.add_widget(self.password)

        login_btn = Button(text='Login')
        login_btn.bind(on_press=self.login)

        layout.add_widget(login_btn)

        self.add_widget(layout)

    def login(self, instance):
        self.manager.current = 'home'


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text='Welcome to ZYKAZ'))

        products_btn = Button(text='View Products')
        products_btn.bind(on_press=self.go_products)

        layout.add_widget(products_btn)

        self.add_widget(layout)

    def go_products(self, instance):
        self.manager.current = 'products'


class ProductsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Images
        layout.add_widget(Image(source='assets/images/dress.jpg'))
        dress_btn = Button(text='Dress - ₹999')
        dress_btn.bind(on_press=self.add_cart)
        layout.add_widget(dress_btn)

        layout.add_widget(Image(source='assets/images/top.jpg'))
        top_btn = Button(text='Top - ₹499')
        top_btn.bind(on_press=self.add_cart)
        layout.add_widget(top_btn)

        layout.add_widget(Image(source='assets/images/jeans.jpg'))
        jeans_btn = Button(text='Jeans - ₹1299')
        jeans_btn.bind(on_press=self.add_cart)
        layout.add_widget(jeans_btn)

        cart_btn = Button(text='Go To Cart')
        cart_btn.bind(on_press=self.go_cart)
        layout.add_widget(cart_btn)

        self.add_widget(layout)

    def add_cart(self, instance):
        global cart_items
        cart_items.append(instance.text)
        print(cart_items)

    def go_cart(self, instance):
        self.manager.current = 'cart'



class CartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        layout.add_widget(Label(text='My Cart', font_size=25))

        global cart_items

        if len(cart_items) == 0:
            layout.add_widget(Label(text='Your cart is empty'))
        else:
            for item in cart_items:
                layout.add_widget(Label(text=item))

        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'products'

    

class ZykazApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProductsScreen(name='products'))
        sm.add_widget(CartScreen(name='cart'))
        return sm


ZykazApp().run()