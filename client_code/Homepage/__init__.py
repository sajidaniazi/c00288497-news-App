from ..ArticleEdit import ArticleEdit
from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_article_button_click(self, **event_args):
    # Initialise an empty dictionary to store the user inputs
    new_article = {}
    # Open an alert displaying the 'ArticleEdit' Form
    save_clicked = alert(
      content=ArticleEdit(item=new_article),
      title="Add Article",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      print(new_article)