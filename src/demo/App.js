/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import {SuggestionsInput} from '../lib';

class App extends Component {
    constructor() {
        super();
        this.state = {
            value: '',
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <SuggestionsInput
                    suggestions={[
                        {
                            trigger: '$',
                            options: [
                                {
                                    value: 'Rambo',
                                    description: 'Bob description',
                                },
                                {
                                    value: 'Terminator',
                                    description: 'Arnold description',
                                },
                            ],
                        },
                    ]}
                />
            </div>
        );
    }
}

export default App;
