# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Pager(Component):
    """A Pager component.
Paging for dash apps.

Keyword arguments:
- total_items (number; optional): The total items in the set.
- page_style (dict; optional): Style for the page numbers.
- style (dict; optional)
- pages_displayed (number; optional): The number of pages displayed by the pager.
- pages (list; optional): Read only, the currently displayed pages numbers.
- page_className (string; optional): CSS class for the page numbers.
- total_pages (number; optional): Set by total_items / items_per_page
- start_offset (number; optional): The starting index of the current page
Can be used to slice data eg: data[start_offset: end_offset]
- current_page (number; optional): The current selected page.
- className (string; optional)
- items_per_page (number; optional): The number of items a page contains.
- end_offset (number; optional): The end index of the current page.
- id (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, total_items=Component.UNDEFINED, page_style=Component.UNDEFINED, style=Component.UNDEFINED, pages_displayed=Component.UNDEFINED, page_className=Component.UNDEFINED, total_pages=Component.UNDEFINED, start_offset=Component.UNDEFINED, pages=Component.UNDEFINED, className=Component.UNDEFINED, items_per_page=Component.UNDEFINED, end_offset=Component.UNDEFINED, current_page=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['total_items', 'page_style', 'style', 'page_className', 'pages_displayed', 'total_pages', 'start_offset', 'current_page', 'className', 'items_per_page', 'id', 'end_offset', 'pages']
        self._type = 'Pager'
        self._namespace = 'dash_extra_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['total_items', 'page_style', 'style', 'page_className', 'pages_displayed', 'total_pages', 'start_offset', 'current_page', 'className', 'items_per_page', 'id', 'end_offset', 'pages']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Pager, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Pager(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Pager(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
