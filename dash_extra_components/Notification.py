# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Notification(Component):
    """A Notification component.


Keyword arguments:
- id (string; optional)
- permission (a value equal to: 'denied', 'granted', 'default', 'unsupported'; optional): Permission granted by the user (READONLY)
- title (string; required)
- lang (string; optional): The notification's language, as specified using a DOMString representing a BCP 47 language tag.
- body (string; optional): A DOMString representing the body text of the notification, which will be displayed below the title.
- badge (string; optional): A USVString containing the URL of the image used to represent the notification when there is not enough space to display the notification itself.
- tag (string; optional): A DOMString representing an identifying tag for the notification.
- icon (string; optional): A USVString containing the URL of an icon to be displayed in the notification.
- image (string; optional): a USVString containing the URL of an image to be displayed in the notification.
- vibrate (number | list; optional): A vibration pattern for the device's vibration hardware to emit when the notification fires.
- require_interaction (boolean; optional): Indicates that a notification should remain active until the user clicks or dismisses it, rather than closing automatically. The default value is false.
- displayed (boolean; optional)
- n_clicks (number; optional)
- n_clicks_timestamp (number; optional)
- n_closes (number; optional)
- n_closes_timestamp (number; optional)
- key (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, permission=Component.UNDEFINED, title=Component.REQUIRED, lang=Component.UNDEFINED, body=Component.UNDEFINED, badge=Component.UNDEFINED, tag=Component.UNDEFINED, icon=Component.UNDEFINED, image=Component.UNDEFINED, vibrate=Component.UNDEFINED, require_interaction=Component.UNDEFINED, displayed=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, n_closes=Component.UNDEFINED, n_closes_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'permission', 'title', 'lang', 'body', 'badge', 'tag', 'icon', 'image', 'vibrate', 'require_interaction', 'displayed', 'n_clicks', 'n_clicks_timestamp', 'n_closes', 'n_closes_timestamp', 'key']
        self._type = 'Notification'
        self._namespace = 'dash_extra_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'permission', 'title', 'lang', 'body', 'badge', 'tag', 'icon', 'image', 'vibrate', 'require_interaction', 'displayed', 'n_clicks', 'n_clicks_timestamp', 'n_closes', 'n_closes_timestamp', 'key']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['title']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Notification, self).__init__(**args)
