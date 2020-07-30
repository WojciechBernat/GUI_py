# Some of the code will be the same as the one above,
# so make sure that you understand that before moving
# to this part

import wx
import operator

# We make a class for frame, so that each time we create a new frame,
# we can simply create a new object for it

class WordPlay(wx.Frame):
    def __init__(self, parent, title):
        super(WordPlay, self).__init__(parent, title=title)
        self.widgets()
        self.Show()

    # Declare a function to add new buttons, icons, etc. to our app
    def widgets(self):
        text_box = wx.BoxSizer(wx.VERTICAL)

        self.textbox = wx.TextCtrl(self, style=wx.TE_RIGHT)
        text_box.Add(self.textbox, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=20)

        grid = wx.GridSizer(2, 1, 10)  # Values have changed to make adjustments to button positions
        button_list = ['Count Words', 'Most Repeated Word']  # List of button labels

        for lab in button_list:
            button = wx.Button(self, -1, lab)  # Initialise a button object
            self.Bind(wx.EVT_BUTTON, self.event_handler, button)
            grid.Add(button, 0, wx.EXPAND)  # Add a new button to the grid with the label from button_list

        text_box.Add(grid, proportion=5, flag=wx.EXPAND, border=20)

        self.SetSizer(text_box)

    def event_handler(self, event):
        # Get label of the button clicked
        btn_label = event.GetEventObject().GetLabel()

        # Get the text entered by user
        text_entered = self.textbox.GetValue()

        # Split the sentence into words
        words_list = text_entered.split()

        # Perform different actions based on different button clicks
        if btn_label == "Count Words":
            result = len(words_list)
        elif btn_label == "Most Repeated Word":
            # Declare an empty dictionary to store all words and
            # the number of times they occur in the text
            word_dict = {}

            for word in words_list:
                # Track count of each word in our dict
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

                # Sort the dict in descending order so that the
                # most repeated word is at the top
                sorted_dict = sorted(word_dict.items(),
                                    key=operator.itemgetter(1),
                                    reverse=True)

                # First value in the dict would be the most repeated word
                result = sorted_dict[0]

        # Set the value of the text box as the result of our computation
        self.textbox.SetValue(str(result))

def main():
    myapp = wx.App()
    WordPlay(None, title='Word Play')
    myapp.MainLoop()

main()