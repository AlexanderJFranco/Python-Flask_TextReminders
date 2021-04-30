# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client






import datetime
import time
timestamp = datetime.datetime.now().time() # Throw away the date information
time.sleep(1)
dict ={}
#if (datetime.datetime.now().time() > timestamp):
#  account_sid = 'AC88c364d72d3a6770433809ca9d4c41f5'
#  auth_token = 'ced1abad470e156c4d8529db603e8171'
#  client = Client(account_sid, auth_token)
#  client.messages.create(
#    to="Your Number",
#    from_="Bot Number",
#    body="This is a bot")



class LoginScreen(GridLayout):
  def __init__(self, **var_args):
    super(LoginScreen, self).__init__(**var_args)
    # super function can be used to gain access
    # to inherited methods from a parent or sibling class
    # that has been overwritten in a class object.
    self.cols = 2  # You can change it accordingly
    self.reminderdate = TextInput()

    # multiline is used to take
    # multiline input if it is true
    self.message = TextInput()
    self.add_widget(self.reminderdate)
    self.add_widget(self.message)
    # password true is used to hide it
    # by * self.add_widget(self.password)
    btn1 = Button(text='Hello World 1')
    btn1.bind(on_press= self.hello_wrld)
    self.add_widget(btn1)
   # self.add_widget(CalendarWidget())

  def hello_wrld(self):

    print('Test')

class MyApp(App):


  def build(self):
    #calendar()
    return LoginScreen()


MyApp().run()
