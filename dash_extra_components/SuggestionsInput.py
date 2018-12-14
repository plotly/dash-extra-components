# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SuggestionsInput(Component):
    """A SuggestionsInput component.
An `<input>`/<textarea> with associated triggers that will display a menu
with suggestions.

Keyword arguments:
- suggestions_style (dict; optional): Given and merged with the default style to the suggestions modal.
- style (dict; optional): Style object given to the container of the input and suggestions modal.
- suggestion_selected_style (dict; optional): Style of a suggestion while it is selected.
- suggestion_className (string; optional): CSS class for a single suggestion element.
- suggestion_style (dict; optional): Style of the suggestion elements (single suggestion).
- allow_space_in_suggestions (boolean; optional): Continue capturing the input when a space is entered while
the suggestion menu is open.
- setProps (boolean | number | string | dict | list; optional)
- suggestions (list; required): Suggestions array containing the options to show
when a trigger is activated.
- value (string; optional): Current value of the input/textarea
- current_trigger (string; optional): The current trigger. (READONLY)
- className (string; optional): CSS class for the container of the input and suggestions modal.
- suggestion_selected_className (string; optional): CSS class for a suggestion while it is selected.
- include_trigger (boolean; optional): Include the trigger in the rendered value.
- filtered_options (list; optional): Currently displayed suggestions. Update in a callback to set the currently displayed suggestions.

@example
```
app.callback(Output('suggestions', 'filtered_options'),
             [Input('suggestions', 'captured')],
             [State('suggestions', 'current_trigger')]
```
- multi_line (boolean; optional): true -> <textarea>
false -> <input>
- fuzzy (string; optional): If true match all options containing the captured input
else match suggestions from the start of the line.
- suggestions_className (string; optional): Given to the suggestions modal.
- id (string; optional)
- captured (string; optional): Readonly prop containing the typed string since the last trigger. (READONLY)

Available events: """
    @_explicitize_args
    def __init__(self, suggestions_style=Component.UNDEFINED, style=Component.UNDEFINED, suggestion_selected_style=Component.UNDEFINED, suggestion_className=Component.UNDEFINED, suggestion_style=Component.UNDEFINED, allow_space_in_suggestions=Component.UNDEFINED, suggestions=Component.REQUIRED, value=Component.UNDEFINED, current_trigger=Component.UNDEFINED, className=Component.UNDEFINED, suggestion_selected_className=Component.UNDEFINED, include_trigger=Component.UNDEFINED, filtered_options=Component.UNDEFINED, multi_line=Component.UNDEFINED, fuzzy=Component.UNDEFINED, suggestions_className=Component.UNDEFINED, id=Component.UNDEFINED, captured=Component.UNDEFINED, **kwargs):
        self._prop_names = ['className', 'style', 'suggestion_selected_style', 'suggestion_className', 'suggestion_style', 'allow_space_in_suggestions', 'suggestions', 'value', 'id', 'suggestions_style', 'suggestion_selected_className', 'include_trigger', 'captured', 'multi_line', 'suggestions_className', 'fuzzy', 'setProps', 'current_trigger', 'filtered_options']
        self._type = 'SuggestionsInput'
        self._namespace = 'dash_extra_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['className', 'style', 'suggestion_selected_style', 'suggestion_className', 'suggestion_style', 'allow_space_in_suggestions', 'suggestions', 'value', 'id', 'suggestions_style', 'suggestion_selected_className', 'include_trigger', 'captured', 'multi_line', 'suggestions_className', 'fuzzy', 'setProps', 'current_trigger', 'filtered_options']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in [u'suggestions']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(SuggestionsInput, self).__init__(**args)

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
            return ('SuggestionsInput(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'SuggestionsInput(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
