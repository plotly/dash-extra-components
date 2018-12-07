# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TableOfContents(Component):
    """A TableOfContents component.
Build a table of contents list with links to the headers tag.

Keyword arguments:
- style (dict; optional): Style of the parent <ul>
- table_of_contents (list; optional): The table of content in object form.
- content_selector (string; optional): Selector to search for building the toc.
- className (string; optional): className for the top ul component.
- headings (list; optional): Headings tag name to search.
The table of contents will be leveled according to the order of
the headings prop.
- setProps (boolean | number | string | dict | list; optional)
- id (string; optional): Unique identifier for the component.

Available events: """
    @_explicitize_args
    def __init__(self, style=Component.UNDEFINED, table_of_contents=Component.UNDEFINED, content_selector=Component.UNDEFINED, className=Component.UNDEFINED, headings=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['style', 'table_of_contents', 'content_selector', 'className', 'headings', 'setProps', 'id']
        self._type = 'TableOfContents'
        self._namespace = 'dash_extra_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['style', 'table_of_contents', 'content_selector', 'className', 'headings', 'setProps', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TableOfContents, self).__init__(**args)

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
            return ('TableOfContents(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'TableOfContents(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
