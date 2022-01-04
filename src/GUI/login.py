from kivy.uix.relativelayout import RelativeLayout


class LoginWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        # managing menu clicks , (in the super i put RelativeLayout to avoid circular imports)
        return super(RelativeLayout, self).on_touch_down(touch)