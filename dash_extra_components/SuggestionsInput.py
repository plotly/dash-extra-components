# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SuggestionsInput(Component):
    """A SuggestionsInput component.
An `<input>`/<textarea> with associated triggers that will display a menu
with suggestions.

Keyword arguments:
- id (string; optional)
- className (string; optional): CSS class for the container of the input and suggestions modal.
- style (dict; optional): Style object given to the container of the input and suggestions modal.
- multi_line (boolean; optional): true -> <textarea>
false -> <input>
- value (string; optional): Current value of the input/textarea
- suggestions (list; required): Suggestions array containing the options to show
when a trigger is activated.
- allow_space_in_suggestions (boolean; optional): Continue capturing the input when a space is entered while
the suggestion menu is open.
- include_trigger (boolean; optional): Include the trigger in the rendered value.
- suggestions_className (string; optional): Given to the suggestions modal.
- suggestions_style (dict; optional): Given and merged with the default style to the suggestions modal.
- suggestion_style (dict; optional): Style of the suggestion elements (single suggestion).
- suggestion_className (string; optional): CSS class for a single suggestion element.
- suggestion_selected_style (dict; optional): Style of a suggestion while it is selected.
- suggestion_selected_className (string; optional): CSS class for a suggestion while it is selected.
- captured (string; optional): Readonly prop containing the typed string since the last trigger. (READONLY)
- filtered_options (list; optional): Currently displayed suggestions. Update in a callback to set the currently displayed suggestions.

@example
```
app.callback(Output('suggestions', 'filtered_options'),
             [Input('suggestions', 'captured')],
             [State('suggestions', 'current_trigger')]
```
- current_trigger (string; optional): The current trigger. (READONLY)
- fuzzy (string; optional): If true match all options containing the captured input
else match suggestions from the start of the line.
- triggerless (boolean; optional): Send suggestions for every keystroke.
- setProps (boolean | number | string | dict | list; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, multi_line=Component.UNDEFINED, value=Component.UNDEFINED, suggestions=Component.REQUIRED, allow_space_in_suggestions=Component.UNDEFINED, include_trigger=Component.UNDEFINED, suggestions_className=Component.UNDEFINED, suggestions_style=Component.UNDEFINED, suggestion_style=Component.UNDEFINED, suggestion_className=Component.UNDEFINED, suggestion_selected_style=Component.UNDEFINED, suggestion_selected_className=Component.UNDEFINED, captured=Component.UNDEFINED, filtered_options=Component.UNDEFINED, current_trigger=Component.UNDEFINED, fuzzy=Component.UNDEFINED, triggerless=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'multi_line', 'value', 'suggestions', 'allow_space_in_suggestions', 'include_trigger', 'suggestions_className', 'suggestions_style', 'suggestion_style', 'suggestion_className', 'suggestion_selected_style', 'suggestion_selected_className', 'captured', 'filtered_options', 'current_trigger', 'fuzzy', 'triggerless', 'setProps']
        self._type = 'SuggestionsInput'
        self._namespace = 'dash_extra_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'className', 'style', 'multi_line', 'value', 'suggestions', 'allow_space_in_suggestions', 'include_trigger', 'suggestions_className', 'suggestions_style', 'suggestion_style', 'suggestion_className', 'suggestion_selected_style', 'suggestion_selected_className', 'captured', 'filtered_options', 'current_trigger', 'fuzzy', 'triggerless', 'setProps']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['suggestions']:
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
