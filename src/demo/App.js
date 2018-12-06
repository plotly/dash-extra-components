/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { DashExtraComponents } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
            </div>
        )
    }
}

export default App;
