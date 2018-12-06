# CONTRIBUTING

Got an awesome project to share with the dash community ? We accept any kind
of components here, submit a PR with your component and it'll be reviewed
by the dash core development team!

## Coding Style

Please lint any additions to react components with `npm run lint`. Rules are defined in [.eslintrc](.eslintrc).

We also use prettier styling, format your code with prettier before submitting a PR. This allows us to focus on the code during reviews instead of styling. [.prettierrc](.prettierrc)

Python code should be linted with flake8 and pylint.

### Adding new components/features

Before submitting a PR, make sure that your component have test app in `test_apps` and there is an automated test (using the app) in `tests`.
We won't review it unless you include at least a basic test demonstrating your component feature and an app we can run.

1. Create the PR.
    - Tag the plotly team in the opening message.
    - Tag a dash core developer or a [contributor](https://github.com/plotly/dash-extra-components/graphs/contributors) for review:
        - @T4rk1n
        - @valentijnnieman
        - @Marc-Andre-Rivet
    - Include a small summary of the components props and basic usage example.

2. After a review has been done and your changes have been approved, create a prerelease and comment in the PR. Version numbers should follow [semantic versioning](https://semver.org/). To create a prerelease:
    * Replace the `__version__` in `./dash_extra_components/__init__.py` with your rc version without `-`. (e.g `"0.13.0rc1"`) 
    * Add `-rc1` to `package.json` e.g. `0.13.0-rc1`
    * Update the `unpkg` link in `./dash_extra_components/__init__.py`, replacing `__version__` with your release candidate (e.g. `"0.13.0-rc1"`)
    * Run `npm run publish-all`.
        - If needed, ask @chriddyp to get NPM / PyPi package publishing access or ask your reviewer.
        - If the `publish-all` script fails on the `twine` command, try running
            ```sh
            twine upload dist/dash_extra_components-X.X.X.tar.gz # where xx.x.x is the version number
            ```
3. Comment in the PR with the prerelease version
4. Update the top-level comment to include info about how to install, a summary of the changes, and a simple example. For a good example, see the [Confirmation Modal component](https://github.com/plotly/dash-core-components/pull/211#issue-195280462).
    * This makes it easier for a community member to come in and try it out. As more folks review, it's harder to find the installation instructions deep in the PR
    * Keep this top-level comment updated with installation instructions (e.g. the `pip install` command)
5. Make a post in the [Dash Community Forum](https://community.plot.ly/c/dash)
    * Title it `":mega: Announcement! New <Your Feature> - Feedback Welcome"`
    * In the description, link to the PR and any relevant issue(s)
    * Pin the topic so that it appears at the top of the forum for two weeks
    * For a good example, see the [Confirmation Modal announcement](https://community.plot.ly/t/announcing-dash-confirmation-modal-feedback-welcome/11627)

## Financial Contributions

If your company wishes to sponsor development of open source dash components, please [get in touch](https://plot.ly/products/consulting-and-oem).