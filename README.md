# dash-extra-components

This package provides extra React components for [Dash][1].

**Why Dash Extra Components?**

[Dash Core Components][3] is our "essential" component suite for Dash. Not all components make the cut!
Dash Extra Components is a more specialized collection of components written by Plotly. Some components were created for our own projects (`dec.TableOfContents` was written for the [Dash User Guide][2]) while others were made for our [Dash Deployment Server](http://plot.ly/dash/pricing/) customers (e.g. `dec.SuggestionsInput`).
Instead of creating a separate repository for each component, we decided to bundle them as a new package to ease discoverability and maintenance.

Dash Extra Components are maintained by Plotly. However, we don't view them quite as essential as our other Dash components and, as such, won't be giving them as much attention with respect to upkeep and documentation. What you see is what you get!

## Installation

`$ pip install dash-extra-components`

## Usage

Importing dash-extra-components:

```python
import dash_extra_components as dec
```

## Development

- Clone the repo.
    `$ git clone https://github.com/plotly/dash-extra-components`
- cd to the project
    `$ cd dash-extra-components`
- Create a virtual named `venv` in order to build the components. The `build:py` command expect a `venv` environment folder in the project root.
    `$ virtualenv venv` or `$ python -m venv venv` for Python 3.
- Install either `requirements.txt` or `tests/requirements` if you want to run the tests locally.
    `$ pip install -r requirements.txt`
- Install npm dependencies.
    `$ npm install`
- Modify/add js code in `src/lib/components`
- Build the components
    `$ npm run build:all`

## Testing

Testing is performed using [pytest-dash][6]. To run the tests locally:

`$ pytest tests --driver Chrome`

Make sure [Chromedriver][5] is available on your PATH.

**make sure to rebuild the components before starting the tests**

### More links

- [Dash][1]
- [Dash documentation][2]
- [Dash community forum][4]
- [Dash core components][3]
- [pytest-dash][6]
- [Dash component boilerplate][7]

[1]: https://github.com/plotly/dash
[2]: https://dash.plot.ly/
[3]: https://github.com/plotly/dash-core-components
[4]: https://community.plot.ly/c/dash
[5]: http://chromedriver.chromium.org/
[6]: https://github.com/T4rk1n/pytest-dash
[7]: https://github.com/plotly/dash-component-boilerplate
